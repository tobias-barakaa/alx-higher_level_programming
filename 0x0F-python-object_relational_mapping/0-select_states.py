#!/usr/bin/python3
"""
This script lists all states from the hbtn_0e_0_usa database.
It takes three command-line arguments:
    - MySQL username
    - MySQL password
    - Database name
The script connects to the MySQL server on the default host (localhost) and port (3306).
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = ("""SELECT * FROM states ORDER BY states.id ASC""")
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
