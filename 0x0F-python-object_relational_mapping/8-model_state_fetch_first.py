#!/usr/bin/python3
"""
prints the first State object from the database
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)

    user = argv[1]
    passw = argv[2]
    db_name = argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passw, db_name),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).first()
    session.close()

    if state is None:
        print("Nothing")
    else:
        print("{:d}: {}".format(state.id, state.name))
