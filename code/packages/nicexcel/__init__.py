"""
Formatting module for Excel files writing
=====

Provides

  - Content: code for writing python files

Available modules
---------------------
:wrapper:
    Module that takes Pandas DataFrame objects and writes them to excel
    in a nicely formatted files:
        - column width auto-adapted to fit characters contained in it
        - filterable Excel columns
        - header freezed by default
        - no indexing by default
        - number formatting of columns according to dataframe data types
        - possibility of specifying number formatting

    Two main functions are available
        - to_excel_nice() --> wrapper of pd.DataFrame.to_excel() function are
            still available because of function wrapping
        - list_to_excel_nice() --> function that writes a dictionary of
            dataframes into one excel file, inserting each dataframe on a
            single sheet. The specifications above still hold and are
            applied on all sheets of the dataframe

:excel_format:
    Lower level module that executes all main formatting functionalities

:const:
    Module that contains all main parameters of module. In general, there is
    no need to modify such constants for a user. It is still possible to modify
    any parameter value via the set_option() method

:utils:
    Module that contains general utility functions for other modules

References
---------------------
:Copyright: None
:License: MIT
"""
# =============================================================================
# Package attributes
# =============================================================================
# Documentation format
__docformat__ = 'NumPy'
# License type
__license__ = 'MIT'
# Status ('Prototype', 'Development' or 'Pre-production')
__status__ = 'Development'
# Version
__version__ = '0.1.12'
# Release date
__releasedate__ = '22/02/2019'


from nicexcel.wrapper import to_excel, to_excel_ms
from nicexcel.utils import set_option
