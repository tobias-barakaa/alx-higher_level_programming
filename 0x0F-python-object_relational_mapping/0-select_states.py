#!/usr/bin/env python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
  db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
  d = db.cursor()
  d.execute("SELECT * FROM states ORDER BY id ASC")
  fetched = d.fetchall()
  for rows in fetched:
    print(rows)
  cursor.close()
  db.close()

