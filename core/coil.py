'''
Core coiling logic.
@AJX 02/2026 - Created
'''

import ast
from utils._zt_string import is_empty_str, EMPTY_STRING
from utils._zt_list import is_empty_list

### Constants ###

COIL_EARMARK = "#@coil@"

### Classes ###

class Boaconstrictor(ast.NodeTransformer):

    def __init__(self, coil_cache: dict[str, ast.AST] = {}) -> None:
        self.coil_cache = coil_cache
    
    def visit_Call(self, node: ast.Call) -> ast.AST:
        return self.coil(node)
    
    def coil(node: ast.Call) -> ast.Call:
        ''' Coils a function call node. '''

### Public API ###

def coil(caller_name: str, call_signature: str, call_args: list[str], coil_sig_body_index: dict[str, str], coil_cache: dict[str, str]) -> str:
    ''' Coils the logic of a caller. '''

    if not __is_proper_input(caller_name, call_signature, call_args):
        return EMPTY_STRING
    
    coil_out = __get_cached_coil(caller_name, call_signature, call_args, coil_cache)
    if not is_empty_str(coil_out):
        return coil_out
    
    body = coil_sig_body_index.get(call_signature, EMPTY_STRING)
    return __perform_coil(body, coil_cache)

### Private APIs ###

def __is_proper_input(caller_name: str, call_signature: str, call_args: list[str]) -> bool:
    ''' Checks if the input is proper for coil.'''
    
    # No caller name, what could we possibly be coiling into?
    if is_empty_str(caller_name):
        return False
    
    # No call signature, what could we possibly be coiling?
    if is_empty_str(call_signature):
        return False
    
    # TODO: currently we won't allow arguments to keep things simple, so only argument-less calls will coil
    if not is_empty_list(call_args):
        return False
    
    return True

__CALL_SIG_KEY = lambda caller_name, call_signature, call_args: (
    f"{caller_name}:{call_signature}:{','.join(call_args)}"
)

def __get_cached_coil(caller_name: str, call_signature: str, call_args: list[str], coil_cache: dict[str, str]) -> str:
    ''' Gets the local coil for the given call. '''
    return coil_cache.get(__CALL_SIG_KEY(caller_name, call_signature, call_args), EMPTY_STRING)

def __set_cached_coil(caller_name: str, call_signature: str, call_args: list[str], coil_out: str, coil_cache: dict[str, str]) -> None:
    ''' Sets the local coil for the given call. '''
    coil_cache[__CALL_SIG_KEY(caller_name, call_signature, call_args)] = coil_out
    
def __perform_coil(body: str, coil_cache: dict[str, str]) -> str:
    ''' Performs the actual coiling logic on the body. '''

    coil_body = EMPTY_STRING

    if is_empty_str(body):
        return EMPTY_STRING
    
    if __is_constant_value(body):
        return body

    if body.startswith("return "):
        return body[len("return "):]
    
    return EMPTY_STRING
    
def __is_constant_value(body: str) -> bool:
    ''' Checks if the body is a constant value. '''

    # Try to parse as int
    try:
        int(body)
        return True
    except ValueError:
        pass
    
    # Try to parse as float
    try:
        float(body)
        return True
    except ValueError:
        pass
    
    # Check for string literals (quoted)
    if (body.startswith('"') and body.endswith('"')) or (body.startswith("'") and body.endswith("'")):
        return True
    
    return False