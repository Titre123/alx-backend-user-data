#!/usr/bin/env python3
""" Session Authentication module for the API.
"""


from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """
        Session Autnentification class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Create session
        """
        if user_id is None or type(user_id) != str:
            return None
        else:
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            get user_id
        """
        if session_id is None or type(session_id) != str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        '''
            get current user
        '''
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return user_id
