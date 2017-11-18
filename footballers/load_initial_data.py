import sqlite3

# run from current directory
# https://docs.python.org/3/library/sqlite3.html

conn = sqlite3.connect('db.sqlite3')
fp = open('../__assets/table_data.sql', 'r')
data = fp.read()
fp.close()

c = conn.cursor()

# https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python
sqlCommands = data.split(';')
for command in sqlCommands:
    try:
        c.execute(command)
    except Exception as msg:
        print(msg)

conn.commit()
conn.close()
