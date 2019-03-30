#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""


if __name__=='__main__':
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

