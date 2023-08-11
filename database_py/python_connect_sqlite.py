# import sql lite

import sqlite3

# connect sql lite
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor() # using cur to control the sql statement

cur.execute('Drop table IF Exists Counts')

cur.execute('''
	Create table Counts (org TEXT, count Integer)''')

fname = input('Enter file name: ')
if len(fname)<1: 
	fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): 
		continue
	pieces = line.split()[1]
	org = pieces.split('@')[1]
	cur.execute('Select count From counts Where org = ?', (org,))
	row = cur.fetchone()

	if row is None:
		cur.execute('Insert into Counts (org, count) Values (?, 1)', (org,))
	else:
		cur.execute('Update Counts SET count = count + 1 Where org = ?', (org,))
sqlstr = 'Select org, count From Counts Order By count DESC LIMIT 10'

print('Counts:')
for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])
cur.close()