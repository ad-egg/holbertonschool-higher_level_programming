#!/usr/bin/python3
"""
takes an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
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
            WHERE name = '{}' COLLATE latin1_general_cs \
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    db.close()
    for row in rows:
        print(row)
