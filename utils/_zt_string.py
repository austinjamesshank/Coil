'''
Utilities for strings.
@AJX 02/2026 - Created
'''

EMPTY_STRING = ""
NEWLINE = "\n"

def is_empty_str(string: str) -> bool:
    ''' Check if a string is none or empty. '''
    return string is None or string == EMPTY_STRING