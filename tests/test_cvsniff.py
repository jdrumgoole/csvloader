import pytest
import csv
from io import StringIO
from csvloader.csvsniff import sniff
from datetime import datetime

# Fixture to create a simulated CSV file using StringIO
@pytest.fixture
def csv_file(tmp_path:str) -> callable(str):
    def _csv_file(content):
        path = tmp_path / "test.csv"
        with open(path, 'w') as f:
            f.write(content)
        return path

    return _csv_file


# Test various column types
def test_column_types(csv_file: callable(str)) -> None:
    content = """id,name,balance,date_registered
123,John Doe,200.50,2021-05-21"""
    file_path = csv_file(content)
    expected = {
        'id': int,
        'name': str,
        'balance': float,
        'date_registered': datetime
    }
    assert sniff(file_path) == expected


# Test with negative and positive integers
def test_signed_integers(csv_file:callable(str)) -> None:
    content = """temperature,pressure,altitude
-15,1013,+350"""
    file_path = csv_file(content)
    expected = {
        'temperature': int,
        'pressure': int,
        'altitude': int
    }
    assert sniff(file_path) == expected


# Test with various date formats
def test_date_formats(csv_file:callable(str)) -> None:
    content = """start_date,end_date
01/02/2020,2020-12-31"""
    file_path = csv_file(content)
    expected = {
        'start_date': datetime,
        'end_date': datetime
    }
    assert sniff(file_path) == expected


# Test for all strings if unable to infer type
def test_all_strings(csv_file:callable(str)) -> None:
    content = """status,description
pending,New order from client"""
    file_path = csv_file(content)
    expected = {
        'status': str,
        'description': str
    }
    assert sniff(file_path) == expected


# Edge cases like empty strings or non-standard data
def test_edge_cases(csv_file:callable(str)) -> None:
    content = """count,price,date
,100.00,Not a date"""
    file_path = csv_file(content)
    expected = {
        'count': str,  # Empty string cannot be inferred
        'price': float,
        'date': str  # Not a valid date format
    }
    assert sniff(file_path) == expected
