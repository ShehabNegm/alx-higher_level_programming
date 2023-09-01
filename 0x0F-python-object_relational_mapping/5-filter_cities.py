#!/usr/bin/python3
"""python script to connect to db using MySQLdb"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                INNER JOIN states \
                ON states.id = cities.state_id \
                WHERE states.name = %s", [argv[4]])
    rows = cur.fetchall()
    L = []
    for row in rows:
        L.append(row[0])
    L = ', '.join(L)
    print(L)

    db.close()