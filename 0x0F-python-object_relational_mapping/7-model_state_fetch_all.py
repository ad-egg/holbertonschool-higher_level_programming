#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""


if __name__=='__main__':
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session
    from sys import argv

    user = argv[1]
    passw = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, passw, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).order_by(State.id.asc()).all()
    session.close()
    for state in states:
        print("{}: {}".format(state.id, state.name))
