#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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

    queries = "SELECT cities.name\
            FROM states JOIN cities ON states.id = cities.state_id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    name = argv[4]
    cursor.execute(queries, (name, ))
    rows = cursor.fetchall()

    for row in rows:
        comma = ','
        print(comma.join(row[0]))

    cursor.close()
    db.close()
