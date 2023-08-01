#!/usr/bin/python3

"""
This is a script that lists all cities from the database hbtn_0e_4_usa
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    queries = "SELECT cities.id, cities.name, states.name\
            FROM states , cities\
            WHERE cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(queries)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
