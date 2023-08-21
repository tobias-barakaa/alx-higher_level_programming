#!/usr/bin/python3

"""
This script lists all `cities` in the `cities` table of the `hbtn_0e_4_usa` database
where the city's state matches the argument `state name`.

The script takes four arguments:
    * The MySQL username
    * The MySQL password
    * The database name
    * The state name to search for

The script connects to the MySQL database on the default host (localhost) and port (3306).

The script uses the `sys` module to get the MySQL username, password, and database name from the command line arguments.

The script uses the `MySQLdb` module to execute the SQL query `SELECT c.name FROM cities c INNER JOIN states s ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id`.

The results of the query are then printed to the console, separated by commas.
"""

import sys
import MySQLdb

def main():
    """
    This function connects to the MySQL database and lists all cities from the cities table where the city's state matches the argument.
    """

    # Get the MySQL username from the command line arguments.
    username = sys.argv[1]

    # Get the MySQL password from the command line arguments.
    password = sys.argv[2]

    # Get the database name from the command line arguments.
    database = sys.argv[3]

    # Get the state name to search for from the command line arguments.
    state_name = sys.argv[4]

    # Connect to the MySQL database.
    connection = MySQLdb.connect(user=username, passwd=password, db=database)

    # Create a cursor object.
    cursor = connection.cursor()

    # Execute the SQL query.
    query = "SELECT c.name FROM cities c INNER JOIN states s ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id"
    cursor.execute(query, (state_name,))

    # Iterate over the results and print each row.
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], end=", ")
    print("")

    # Close the cursor object.
    cursor.close()

    # Close the connection to the database.
    connection.close()

if __name__ == "__main__":
    main()
