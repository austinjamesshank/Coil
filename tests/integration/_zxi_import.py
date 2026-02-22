import importlib


def test_coil_module_imports():
    module = importlib.import_module("core.coil")
    assert module is not None