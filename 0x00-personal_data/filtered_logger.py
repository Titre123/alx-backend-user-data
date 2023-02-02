#!/usr/bin/env python3
'''
    Module to write a function called filter_datum that returns the log
    message obfuscated
'''

import logging
from typing import List, Union
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
    '''
        Args:
            - fields: a list of strings representing all fields to obfuscate
            - redaction: a string representing by what the field will be obfuscated
            - message: a string representing the log line
            - seperator: a string representing by which character is separating
            all fields in the log line (message)
    '''
    new_message = []
    for _ in message.split(separator):
        if _.split('=')[0] in fields:
            new_message.append(
                re.sub(_[re.search(_.split('=')[0], _).span()[1] + 1:], redaction, _))
        else: new_message.append(_)
    return separator.join(new_message)
