import pytest
import csv
from io import StringIO
from csvloader.csvsniff import sniff
from datetime import datetime


# Fixture to create a simulated CSV file using StringIO
@pytest.fixture
def csv_file(tmp_path: str) -> callable(str):
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
