#!/usr/bin/python3
"""
lists all states with a name starting with N from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states \
            WHERE name LIKE 'N%' COLLATE latin1_general_cs \
            ORDER BY states.id ASC")
    rows = cur.fetchall()
    cur.close()
    db.close()
    for row in rows:
        print(row)
