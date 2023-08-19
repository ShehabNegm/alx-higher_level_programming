#!/usr/bin/python3
"""python script to connect to db using MySQLdb"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
