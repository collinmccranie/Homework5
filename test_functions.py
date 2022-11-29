import pytest
from functions import *

@pytest.mark.parametrize("file", ["Not a file", "testing.txt"])

def test_openFile(file):
    assert openFile(file) == None

@pytest.mark.parametrize("file,result", [("Not a file", "There is no file with that name."), ("testing.txt", "File opened.")])

def test_openFileOutput(capsys, file, result):
    openFile(file)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == result

@pytest.mark.parametrize("num1,num2, results", [(6, 3, 2), (6, 0, None), ("cool", "o", None), (6.2, 2, 3.1)])

def test_numbers(num1, num2, results):
    assert numbers(num1, num2) == results
