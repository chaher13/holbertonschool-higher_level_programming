#!/usr/bin/python3

"""
This is  a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    queries = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(queries, (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
