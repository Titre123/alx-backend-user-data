#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
from db import DB

my_db = DB()

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

sess = auth.create_session(email)
print(sess)
print(auth.create_session("unknown@email.com"))

print(auth.get_user_from_session_id(sess).session_id)