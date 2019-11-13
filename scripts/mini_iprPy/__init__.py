"""
Attributes
----------
rootdir : str
    The absolute path to the iprPy package's root directory used to locate
    contained data files.
libdir : str
    The absolute path to the iprPy package's library directory.
"""
# Standard Python libraries
from pathlib import Path

# Define package-specific directories
rootdir = Path(__file__).absolute().parent

# Read version from VERSION file
with open(Path(rootdir, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

__all__ = ['__version__', 'rootdir', 'tools', 'input',
           'record', 'load_record']
__all__.sort()

# iprPy imports
from . import tools
from . import input

from . import record
from .record import load_record