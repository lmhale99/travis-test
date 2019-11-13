# iprPy imports
from .input.subset_classes import loaded as input_subset_loaded
from .input.subset_classes import failed as input_subset_failed
from .record import loaded as record_loaded
from .record import failed as record_failed

__all__ = ['check_modules']

def check_modules():
    """
    Prints lists of the calculation, record, and database styles that were
    successfully and unsuccessfully loaded when iprPy was initialized.
    """
    print('input.subset styles that passed import:')
    for style in input_subset_loaded.keys():
        print(f'- {style}')
    print('input.subset styles that failed import:')
    for style in input_subset_failed.keys():
        print(f'- {style}: {input_subset_failed[style]}')
    print()
    
    print('record styles that passed import:')
    for style in record_loaded.keys():
        print(f'- {style}')
    print('record styles that failed import:')
    for style in record_failed.keys():
        print(f'- {style}: {record_failed[style]}')
    print()