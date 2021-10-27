"""Utility functions."""

__author__ = "730394024"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Preapre to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item) 
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(columns_data: dict[str, list[str]], i: int) -> dict[str, list[str]]:
    """Gives the first 'n' row values, where 'n' is given as a parameter."""
    result: dict[str, list[str]] = {}
    
    for row in columns_data:
        counter: int = 0
        first_values: list[str] = []
        while counter < i:
            first_values.append(columns_data[row][counter])
            counter += 1
        result[row] = first_values
        
    return result 


def select(table: dict[str, list], subset: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with a specific subset of the columns."""
    result: dict[str, list[str]] = {}
    for column in subset:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column based table combining the column based tables given in the parameter."""
    result: dict[str, list[str]] = {}
    for column_1 in table_1:
        result[column_1] = table_1[column_1]
    for column_2 in table_2:
        if column_2 in result:
            result[column_2] += table_2[column_2]
        else:
            result[column_2] = table_2[column_2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Records the frequency of the """
    result: dict[str, int] = {}
    for x in values:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result