import csv
from datetime import datetime

from dateutil import parser as date_parser


def sniff(file_path:str) -> dict[str, type]:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        columns = next(reader)  # Read the first line to get column names
        types = next(reader)  # Read the second line to infer types

        type_dict = {}

        for col, val in zip(columns, types):
            if is_int(val):  # Check if the value is an integer
                type_dict[col] = int
            elif is_float(val):  # Check if the value can be a float
                type_dict[col] = float
            elif is_date(val):  # Check if the value is a date
                type_dict[col] = datetime
            else:
                type_dict[col] = str  # Treat as string if no other type matches

        return type_dict


def is_int(value:str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_float(value:str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_date(value:str) -> bool:
    try:
        date_parser.parse(value)
        return True
    except ValueError:
        return False

# Usage example:
# info = sniff('path_to_your_csv_file.csv')
# print(info)
