#!/usr/bin/python3
"""changes the name of a State object from a database"""


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
    nm = session.query(State).filter_by(id=2).first()
    nm.name = 'New Mexico'
    session.add(nm)
    session.commit()
    session.close()
