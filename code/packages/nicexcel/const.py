

# =============================================================================
# Global public parameters (ALL PARAMETERS MUST BE UPPER CASE)
# =============================================================================
# general constants
MAX_COLUMN_WIDTH = 50
# margin, add a little extra space to each column to make it readable
READABILITY_MARGIN = 5

# =============================================================================
# String for column formatting
# =============================================================================
# percentage columns
NF_PERCENT = ['%', 'percent', 'percentage', '0%']
# openpyxl internal representation of percentage number format
OP_PERCENT = '0%'
# normal columns with 2 decimals and thousands separators
NF_NORMAL = ['0,000.00', '#,##0.00', 'normal', '#,###.00', '#,###.##',
             '0.000,00', '#.##0,00', '#.###,00', '#.###,##', '2 decimals']
# openpyxl internal representation of 2 decimals and thousands separators
OP_NORMAL = '#,###.00'
# normal columns with 0 decimals (integers)
NF_INTEGER = ['0,000', '#,##0', 'integer', '#,###', '#,###', '0.000',
              '#.##0', '#.###', '#.###', 'normal no commas', 'no commas']
# openpyxl internal representation of integers (no decimals) and thousands
OP_INTEGER = '#,##0'


# for all variables here there should be a
# nl.set_option(parameter, value)



