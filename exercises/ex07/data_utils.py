"""Dictionary related utility functions."""

__author__ = "730466380"

from csv import DictReader 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'col_table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(col_table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    result: list[str] = []
    for row in col_table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Trandsform a row-oriented col_table to a column-oriented col_table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(col_table: dict[str, list[str]], num_row: int) -> dict[str, list[str]]:
    """Creating a column based table for certain rows of data."""
    result: dict[str, list[str]] = {}
    for column in col_table:
        col_val: list[str] = []
        i: int = 0
        if num_row >= len(col_table[column]):
            return col_table
        else:
            while i < num_row:
                col_val.append(col_table[column][i])
                i += 1
        result[column] = col_val
        return result


def select(col_table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    """Making a column-based table with only specific parts of the original columns."""
    result: dict[str, list[str]] = {}
    for column in col_name:
        result[column] = col_table[column]
    return result
    

def concat(col_table_1: dict[str, list[str]], col_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Make column based table with two columns combined into one."""
    result: dict[str, list[str]] = {}
    for column in col_table_1:
        result[column] = col_table_1[column]
    for column in col_table_2:
        if column in result:
            result[column] = col_table_2[column]
        else:
            for val in col_table_2[column]:
                result[column].append(val)
        return result


def count(freq: list[str]) -> dict[str, int]:
    """Number of times a value appears on the list."""
    result: dict[str, int] = {}
    for item in freq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
