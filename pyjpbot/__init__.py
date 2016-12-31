import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
from . models import *

engine=None
def session_factory():
    return sessionmaker(bind=engine)

session = scoped_session(sessionmaker())

def init():
    global engine
    # 'postgresql://scott:tiger@localhost/mydatabase'
    url = os.environ.get('PYJPBOT_DBURL', 'sqlite:///pyjpbot.sqlite')
    engine = create_engine(url)
    session.configure(bind=engine)

def create_table():
    Base.metadata.create_all(engine)

    