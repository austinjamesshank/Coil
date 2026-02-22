'''
Testing utilities for accessing module members.
@AJX 02/2026 - Created
'''

import importlib

def get_module_fxn(module_path, func_name: str):
    """
    Get any function/variable from a module by exact name.
    
    Usage:
        is_constant_value = get_module_fxn('core.coil', '__is_constant_value')
        assert is_constant_value("12") == True
        
        coil_func = get_module_fxn('core.coil', 'coil')
        result = coil_func("caller", "sig", [], {}, {})
    
    Pass the exact name as it appears in the module.
    """

    module = importlib.import_module(module_path)
    
    if not hasattr(module, func_name):
        raise AttributeError(f"No member '{func_name}' in {module_path}")
    
    return getattr(module, func_name)

def exe_module_fxn(module_path, func_name: str, *args, **kwargs):
    """
    Execute any function from a module by exact name with given arguments.
    
    Usage:
        result = exe_module_fxn('core.coil', 'coil', "caller", "sig", [], {}, {})
    
    Pass the exact name as it appears in the module.
    """

    func = get_module_fxn(module_path, func_name)
    
    if not callable(func):
        raise TypeError(f"Member '{func_name}' in {module_path} is not callable")
    
    return func(*args, **kwargs)
