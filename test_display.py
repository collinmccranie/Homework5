import pytest

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])

def test_display():
    assert displayItem([2,4,6,8], 1) == None

def test_display2():
    assert displayItem([1,3,5,7], 3) == None

def test_display3():
    assert displayItem([4,8,12,16,20], 2) == None

def test_display4():
    assert displayItem([10,20,30,40,50,60], 4) == None