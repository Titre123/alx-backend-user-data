#!/usr/bin/env python3
"""Auth module
"""


import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    '''
        hash password
    '''
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
            register a new user to the database
        '''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))

        except (AttributeError, InvalidRequestError):
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)
