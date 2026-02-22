'''
Unit tests for coil.py.
@AJX 02/2026 - Created
'''

from core.coil import coil
from utils._zt_string import is_empty_str
from utils._zt_execute import exe_module_fxn

### Input Validation ###

def test_coil_input_all_empty():
    result = coil("", "", [], {}, {})
    assert is_empty_str(result)

def test_coil_input_empty_caller_name():
    result = coil("", "some_function", [], {}, {})
    assert is_empty_str(result)

def test_coil_input_empty_call_signature():
    result = coil("caller", "", [], {}, {})
    assert is_empty_str(result)

def test_coil_input_with_args_not_allowed():
    result = coil("caller", "some_function", ["arg1"], {}, {})
    assert is_empty_str(result)

### Coil Validation ###

def test_coil_constant_int_validation():
    assert exe_module_fxn("core.coil", "__is_constant_value", "12") == True

def test_coil_constant_int():
    caller_name = "caller"
    call_signature = "CONSTANT_INT"
    call_args = []
    sig_body_index = {
        call_signature: "42"
    }
    coil_cache = {}
    result = coil(caller_name, call_signature, call_args, sig_body_index, coil_cache)
    assert result == "42"

def test_coil_return_constant_int():
    caller_name = "caller"
    call_signature = "return_constant_int"
    call_args = []
    sig_body_index = {
        call_signature: "return 42"
    }
    coil_cache = {}
    result = coil(caller_name, call_signature, call_args, sig_body_index, coil_cache)
    assert result == "42"

def test_coil_constant_string_validation():
    assert exe_module_fxn("core.coil", "__is_constant_value", "'This is a constant string.'") == True

def test_coil_constant_string():
    caller_name = "caller"
    call_signature = "CONSTANT_STRING"
    call_args = []
    sig_body_index = {
        call_signature: "'This is a constant string.'"
    }
    coil_cache = {}
    result = coil(caller_name, call_signature, call_args, sig_body_index, coil_cache)
    assert result == "'This is a constant string.'"

def test_coil_return_constant_string():
    caller_name = "caller"
    call_signature = "return_constant_string"
    call_args = []
    sig_body_index = {
        call_signature: "return 'This is a constant string.'"
    }
    coil_cache = {}
    result = coil(caller_name, call_signature, call_args, sig_body_index, coil_cache)
    assert result == "'This is a constant string.'"