from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, Column, Integer, String, TIMESTAMP

Base = declarative_base()

class PlusMinus(Base):
    __tablename__ = 'plusminus'
    id =  Column(Integer, primary_key=True)
    pointto = Column(String(50), nullable=False, index=True)
    pointfrom = Column(String(50), nullable=False, index=True)
    point = Column(Integer, nullable=False)

    created = Column(TIMESTAMP(), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(), nullable=False, server_default=func.now(), onupdate=func.now())

