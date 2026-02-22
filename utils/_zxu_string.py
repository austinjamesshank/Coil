'''
Unit tests for string utilities.
@AJX 02/2026 - Created
'''

from utils._zt_string import is_empty_str


def test_is_empty_str():
    assert is_empty_str(None) == True
    assert is_empty_str("") == True
    assert is_empty_str(" ") == False
    assert is_empty_str("test") == False
    assert is_empty_str("\n") == False