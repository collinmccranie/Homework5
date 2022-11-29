import pytest
from functions import *

# openFile tests
@pytest.mark.parametrize("file", ["Not a file", "testing.txt"])

def test_openFile(file):
    assert openFile(file) == None

@pytest.mark.parametrize("file,result", [("Not a file", "There is no file with that name."), ("testing.txt", "File opened.")])

def test_openFileOutput(capsys, file, result):
    openFile(file)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == result

# numbers test
@pytest.mark.parametrize("num1,num2, results", [(6, 3, 2), (6, 0, None), ("cool", "o", None), (6.2, 2, 3.1)])

def test_numbers(num1, num2, results):
    assert numbers(num1, num2) == results

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        return dist

    except:
        print("\nWrong type.")

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]

        if (test == temp):
            return True

        else:
            return False
    except:
        print("\nWrong type.")
   
# dist tests

## Pytest - checking that the math for dist works
def test_dist_mathCheck():
    assert dist(4, 4, 8, 7) == 5


def test_dist_mathCheck2():
    assert dist(2, 3, 1, 9) != 5


## PyTest - checking what happens when you enter different types of inputs
def test_dist_typeDouble():
    assert dist(2.5, 4.0, 2.5, 8.0) == 4.0


def test_dist_typeString():
    assert dist("hello", "world", 4, 3) == None


def test_dist_typeInt():
    assert dist(0, 0, 0, 0) == 0

# isPalindrome tests
    
## Pytest checking what happens when you enter different types of inputs
def test_isPalindrome_typeInt():
    assert isPalindrome(1) == None


def test_isPalindrome_typeDouble():
    assert isPalindrome(2.0) == None


def test_isPalindrome_typeStr():
    assert isPalindrome("bob") == True


## Pytest checking if the palindrome function works
def test_isPalindrome_working():
    assert isPalindrome("racecar") == True


def test_isPalindrome_working2():
    assert isPalindrome("pineapple") != True
    
# displayItem test
    
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

# greetUser tests  
    
## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

def test_greet():
    assert greetUser("Collin", "Joseph", "McCranie") == None

def test_greet2():
    assert greetUser("John", "Edward", "Doe") == None

def test_greet3():
    assert greetUser("Jane", "Elizabeth", "Doe") == None

def test_greet4():
    assert greetUser("Jackson", "Chistopher", "Williams") == None
