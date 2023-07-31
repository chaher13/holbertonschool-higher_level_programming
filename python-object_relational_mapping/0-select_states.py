#!/usr/bin/python3

"""
This is a script  that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb


    db  = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
