'''
Logic for parsing .py files and extracting function call information.
@AJX 02/2026 - Created
'''

import ast
from utils._zt_file import is_file_type, read_file_to_list
from utils._zt_list import is_empty_list, pack_list_to_str
from utils._zt_string import EMPTY_STRING, NEWLINE, is_empty_str

def parse_py_file(file_path: str) -> dict[str, any]:
    ''' Parses a .py file and extracts function call information. '''

    if not is_file_type(file_path, ".py"):
        return {}
    
    lines_of_code = read_file_to_list(file_path)
    if is_empty_list(lines_of_code):
        return {}
    
    lines_packed = pack_list_to_str(lines_of_code, NEWLINE)
    if is_empty_str(lines_packed):
        return {}

    tree = ast.parse(lines_packed)
    if tree is None:
        return {}

    return parse_py_tree(tree, lines_packed)

def parse_py_tree(tree: ast.AST, lines_packed: str) -> dict[str, any]:
    ''' Parses an AST tree and extracts function call information. '''

    sig_body_index = {}

    for node in ast.walk(tree):
        
        if not isinstance(node, ast.Call):
            continue
        
        func_name = get_func_name(node.func)
        if is_empty_str(func_name):
            continue
        
        unique_sig = ast.get_source_segment(lines_packed, node)
        sig_body_index[unique_sig] = ""

    return sig_body_index

def get_func_name(node: ast.AST) -> str:
    ''' Gets the function name from an AST node. '''

    if isinstance(node, ast.Name):
        return node.id
    
    if isinstance(node, ast.Attribute):
        return node.attr
        
    return EMPTY_STRING

def __main__():
    ''' Main function for testing. '''
    file_path = "core/coil.py"
    result = parse_py_file(file_path)

if __name__ == "__main__":
    __main__()