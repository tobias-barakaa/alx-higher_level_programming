#!/usr/bin/env python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
Safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Create and execute the query to fetch states matching the given name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
