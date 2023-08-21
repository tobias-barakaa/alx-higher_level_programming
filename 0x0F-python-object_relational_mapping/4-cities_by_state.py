#!/usr/bin/python3

"""
This script lists all `cities` from the database `hbtn_0e_4_usa`.

The script takes three arguments:
    * The MySQL username
    * The MySQL password
    * The database name

The script connects to the MySQL database on the default
host (localhost) and port (3306).

The script uses the `sys` module to get the MySQL username,
password, and database name from the command line arguments.

The script uses the `MySQLdb` module to execute the SQL query
`SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s
ON c.state_id = s.id ORDER BY c.id`.

The results of the query are then printed to the console.

Here is a breakdown of the SQL query:

* `SELECT c.id, c.name, s.name`: This selects the `id`, `name`,
and `name` columns from the `cities` and `states` tables.
* `FROM cities c INNER JOIN states s`: This joins the `cities`
and `states` tables on the `state_id` column.
* `ON c.state_id = s.id`: This specifies the join condition.
* `ORDER BY c.id`: This sorts the results by the `id` column.
"""

import sys
import MySQLdb


def main():
    """
    This function connects to the MySQL database and
    lists all cities from the cities table.
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

    # Execute the SQL query.
    query = "SELECT c.id, c.name,\
    s.name FROM cities c INNER JOIN\
    states s ON c.state_id = s.id ORDER BY c.id"
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
