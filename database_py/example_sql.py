import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor() # using cur to control the sql statement

cur.execute('''DROP TABLE IF EXISTS Counts''') # Drop table Counts purge;

cur.execute('''
	Create table Counts (org TEXT, count INTEGER)''')

# read file
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()[1]
	org = pieces.split('@')[1]
	# now check sql:
	cur.execute('''
		SELECT count FROM Counts Where org = ?''', (org,)) # '?' is a place holder and will replace by org
	row = cur.fetchone()

	# if no record add one:
	if row is None:
		cur.execute('''
			INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
	else: # if record exist then update it
		cur.execute('''
			UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
	conn.commit()

# https://www.splite.org/lang_select.html

# run sql
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])

# close cur
cur.close()