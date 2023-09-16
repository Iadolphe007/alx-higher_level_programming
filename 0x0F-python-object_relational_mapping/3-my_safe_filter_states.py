#!/usr/bin/python3

"""
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, passwd=argv[2],
                         user=argv[1], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
            ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
