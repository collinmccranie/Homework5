import pytest
import math

## returns the squareroot of a particular number
def sq(num):
    if (num != type(int)):
        return -1

    return math.sqrt(num)

def test_sq():
    assert sq(4)

def test_sq2():
    assert sq(15.5)

def test_sq2():
    assert sq("Hello")

def test_sq4():
    assert sq('a')
    
