# Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

# Your script should take 3 arguments: mysql username, mysql password and database name
# You must use the module SQLAlchemy
# You must import State and Base from model_state - from model_state import Base, State
# Your script should connect to a MySQL server running on localhost at port 3306
# Your code should not be executed when imported

#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    a = '%a%'
    del_state = session.query(State).filter_by(State.name.like(a)).first()
    for state in states:
        session.delete(del_state)
    session.commit()
    session.close()