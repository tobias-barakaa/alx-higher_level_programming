#!/usr/bin/python3
"""
Script lists all states from database hbtn_0e_0_usa
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    main()
