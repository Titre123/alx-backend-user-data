#!/usr/bin/env python3
""" Authentication module for the API.
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """
        Auth class for user authentification
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Args:
                path -> str
                excluded_paths
            Return:
                False -> Bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
            Args:
                request
            Return:
                None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Args:
                Request
            Return:
                None
        """
        return None
