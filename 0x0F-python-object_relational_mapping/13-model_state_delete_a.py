#!/usr/bin/python3
# Graham S. Paul (13-model_state_delete_a.py)
"""
Remove from table states with names holding alphabete 'a'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # find all appropriate states to be deleted
    states = session.query(State).filter(State.name.like('%a%')).all()
    for s in states:
        session.delete(s)

    session.commit()
    session.close()
