#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from a database
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
    all_states = session.query(State).order_by(State.id.asc()).all()
    for state_obj in all_states:
        if 'a' in state_obj.name:
            session.delete(state_obj)
    session.commit()
    session.close()
