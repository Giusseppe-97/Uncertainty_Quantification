

import openpyxl as op
import nicexcel.const as const


def get_row_as_str(row: int):
    """
    get integer number as string
    """
    return repr(row)


def read_header(ws: op.worksheet.worksheet.Worksheet,
                max_col: int,
                first_row: int=1):
    """
    returns dictionary containing per each column name (part of header) the
    corresponding column in the resulting Excel workshee
    """
    header_dict = {}
    for col in range(1, max_col+1):
        col_value = ws.cell(row=first_row, column=col).value
        header_dict[col_value] = col
    return header_dict


def set_option(param_name: str, value):
    """
    set value of some parameters in constant file, parameter string is not case
    sensitive. In case of scalar/string, the method modifies variable.
    In case of list, it appends the new value to existing list
    """
    # cast upper case
    par_name_upper = param_name.upper()
    # set new value for specified variable
    try:
        if isinstance(const.__dict__[par_name_upper], list) is False:
            if isinstance(const.__dict__[par_name_upper], dict) is False:
                if 'OP_' != par_name_upper[0:3]:
                    const.__dict__[par_name_upper] = value
                    return None
        # append value to existing list
        else:
            const.__dict__[par_name_upper] = value
            return None
        # notify user
        print("Can't modify " + param_name + " parameter value")
    except KeyError:
        print('Parameter ' + param_name + 'not existent')
