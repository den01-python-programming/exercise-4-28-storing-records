import pytest
from src.exercise import read_records_from_file

def test_exercise(capsys):
    file = "data.txt"
    records = read_records_from_file(file)

    assert records == ["lily","anton","levi","amy"]
