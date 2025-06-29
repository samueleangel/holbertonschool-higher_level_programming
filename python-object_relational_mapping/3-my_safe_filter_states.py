#!/usr/bin/python3
# Prints all rows from the 'states' table in the hbtn_0e_0_usa database
# where the name matches the one given as argument.
# This version is safe against SQL injection.
# How to run:
# ./3-my_safe_filter_states.py <username> <password> <database_name> <state_name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
