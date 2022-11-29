import pytest

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
    except TypeError:
        print("Input must be an integer")
        return

    try:
        num2 = int(input("Enter another number: "))
    except TypeError:
        print("Input must be an integer")
        return
    
    try:
        div = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return

    print("Your numbers divided is:", div)

def geninputs():
    inputs = [9,3]

    for item in inputs:
        yield item

GEN = geninputs()

def test_divide(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    assert divide() == None



def geninputs2():
    inputs = [9,3.5]

    for item in inputs:
        yield item

GEN2 = geninputs2()

def test_divide2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))
    assert divide() == None



def geninputs3():
    inputs = ["Hello",3.5]

    for item in inputs:
        yield item

GEN3 = geninputs3()

def test_divide3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN3))
    assert divide() == None
