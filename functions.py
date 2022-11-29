import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")

    except FileNotFoundError:
        print("There is no file with that name.")

    else:
        print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        result = num1 / num2

    except TypeError:
        print("Input must be two numbers.")

    except ZeroDivisionError:
        print("Cannot divide by 0.")

    else:
        return result

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

## returns the squareroot of a particular number
def sq(num):
    if (num != type(int)):
        return -1

    return math.sqrt(num)
    
## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", str(first), str(middle), str(last))
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if (index == type(int)):
        print("Your item at", int(index), "index is", list(numbers[index]))
