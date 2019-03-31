#!/usr/bin/python3
"""
prints the state object with the name passed as argument
"""

if __name__ == '__main__':
    from model_state import Base, State
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
    state = session.query(State).filter(State.name == argv[4]).first()
    session.close()

    if state is None:
        print("Not found")
    else:
        print("{:d}".format(state.id))
