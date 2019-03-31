#!/usr/bin/python3
"""prints all City objects from a database"""


if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session
    from sys import argv

    user = argv[1]
    passw = argv[2]
    db_name = argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passw, db_name),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    joined = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id.asc()).all()
    session.close()

    for cities, states in joined:
        print("{}: ({:d}) {}".format(states.name, cities.id, cities.name))
