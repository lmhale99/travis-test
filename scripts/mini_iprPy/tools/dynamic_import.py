# Standard Python libraries
import sys
from pathlib import Path
from importlib import import_module

def dynamic_import(module_file, module_name, ignorelist=None):
    """
    Dynamically imports classes stored in submodules and makes them directly
    accessible by style name within the returned loaded dictionary.
    
    Parameters
    ----------
    
    Returns
    -------
    loaded : dict
        Contains the derived classes that were successfully loaded and
        accessible by style name (root submodule).
    failed : dict
        
    """
    if ignorelist is None:
        ignorelist = []
    names = []
    parent = Path(module_file).parent
    ignorelist = ['__init__', '__pycache__'] + ignorelist
    loaded = {}
    failed = {}
    
    for child in parent.iterdir():
        if child.is_dir():
            name = child.name
            if name not in ignorelist:
                names.append(name)
        
        elif child.is_file():
            name = child.stem
            ext = child.suffix
            
            if ext.lower() in ('.py', '.pyc'):
                if name not in ignorelist and name not in names:
                    names.append(name)
    
    for name in names:
        try:
            module = import_module('.' + name, module_name)
            all = getattr(module, '__all__')
            if len(all) != 1:
                raise AttributeError("module's __all__ must have only one attribute")
        except:
            failed[name] = '%s: %s' % sys.exc_info()[:2]
        else:
            loaded[name] = getattr(module, all[0])
    
    return loaded, failed