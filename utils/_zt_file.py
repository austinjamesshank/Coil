'''
File utility functions.
@AJX 02/2026 - Created
'''

from utils._zt_list import is_empty_list
from utils._zt_string import is_empty_str
    
def read_file_to_list(file_path: str) -> list[str]:
    ''' Reads a file and returns its contents as an array of lines. '''

    if is_empty_str(file_path):
        return []
    
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    
def is_empty_file(file_path: str) -> bool:
    ''' Check if a file is empty. '''
    return is_empty_list(read_file_to_list(file_path))

def is_file_type(file_path: str, extension: str) -> bool:
    ''' Check if a file is of a certain type based on its extension. '''
    return file_path.endswith(extension)