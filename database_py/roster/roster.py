import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

try:
    with open(fname) as file:
        data = json.load(file)

    for entry in data:
        if len(entry) != 3:
            print("Invalid data format:", entry)
            continue

        name, title, role = entry
        print((name, title, role))

        cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name,))
        cur.execute('SELECT id FROM User WHERE name = ?', (name,))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title,))
        cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''',
                    (user_id, course_id, role))

        conn.commit()

except FileNotFoundError:
    print(f"File '{fname}' not found.")
except json.JSONDecodeError:
    print(f"Invalid JSON data in '{fname}'.")
except sqlite3.Error as e:
    print("An error occurred while interacting with the database:", str(e))
finally:
    conn.close()
