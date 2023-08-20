#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.

The script takes three arguments:
    * The MySQL username
    * The MySQL password
    * The database name

The script connects to the MySQL database on the default host (localhost) and port (3306).

The script prints the results of the query to the console.
"""

import sys
import MySQLdb

def main():
    """
    This function connects to the MySQL database and lists all states.
    """

    # Get the MySQL username from the command line arguments.
    username = sys.argv[1]

    # Get the MySQL password from the command line arguments.
    password = sys.argv[2]

    # Get the database name from the command line arguments.
    database = sys.argv[3]

    # Connect to the MySQL database.
    connection = MySQLdb.connect(user=username, passwd=password, db=database)

    # Create a cursor object.
    cursor = connection.cursor()

    # Execute the SQL query to select all states.
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Iterate over the results and print each row.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor object.
    cursor.close()

    # Close the connection to the database.
    connection.close()

if __name__ == "__main__":
    main()
