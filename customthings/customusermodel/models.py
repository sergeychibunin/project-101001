from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy_utils import EmailType

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class CUser(Base):
    __tablename__ = 'cuser'
    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=False)
    mname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    bday = Column(Date, nullable=False)
    email = Column(EmailType, nullable=False)
    phash = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
