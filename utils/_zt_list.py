'''
Utility functions for lists.
@AJX 02/2026 - Created
'''

def is_empty_list(lst: list[any]) -> bool:
    ''' Check if a list is none or empty. '''
    return lst is None or len(lst) == 0

def pack_list_to_str(lst: list[any], delimiter: str = ",") -> str:
    ''' Packs a list into a string. '''
    return delimiter.join(str(item) for item in lst)