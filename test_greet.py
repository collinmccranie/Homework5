import pytest

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", str(first), str(middle), str(last))
    print("Glad to have you!")

def test_greet():
    assert greetUser("Collin", "Joseph", "McCranie") == None

def test_greet2():
    assert greetUser(2, "Edward", "Doe") == None

def test_greet3():
    assert greetUser("Jane", "Elizabeth", "Doe") == None

def test_greet4():
    assert greetUser(1.0, "Chistopher", "Williams") == None