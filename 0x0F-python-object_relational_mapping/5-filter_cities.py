#!/usr/bin/python3
"""
This file lists all cities from a state from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id=states.id \
            WHERE states.name=%s ORDER BY cities.id ASC", (argv[4],))
    city_names = cur.fetchall()
    cur.close()
    db.close()
    names_list = []
    for city_name in city_names:
        names_list.append(city_name[0])
    print(*names_list, sep=", ")
