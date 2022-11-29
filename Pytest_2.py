import math
import pytest


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

