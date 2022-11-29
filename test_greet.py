import pytest

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