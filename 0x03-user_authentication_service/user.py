#!/usr/bin/env python3
'''
    User Model Using SqlAlchelmy
'''


from flask import Flask
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create application
app = Flask(__name__)

# declare base from Models
Base = declarative_base()

# create sqlalchemy engine
engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    '''
        Class User inheriting from Base
        It create User Models
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
