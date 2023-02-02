#!/usr/bin/env python3
'''
    Module to write a function called filter_datum that returns the log
    message obfuscated
'''

import logging
from typing import List, Union
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Filters a log line '''
    new_message = [re.sub(_[re.search(_.split('=')[0], _).span()[1] + 1:],
                   redaction, _)if _.split('=')[0] in fields else _ for _ in
                   message.split(separator)]
    return separator.join(new_message)
