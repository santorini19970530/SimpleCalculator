# SimpleCalculator

def printScreen():
    print("\nA : Addition\nB : Subtraction\nC : Multipication\nD : Division\n")

def getInputs():
    try:
        x, y = input("Input two integers (in [digit_one digit_two] format) >> ").split()
        userInput = (int(x), int(y))
    except ValueError:
        return None
    else:
        return userInput

def add(x, y):
    print(f"{x} + {y} = {x + y}")

def subtract(x, y):
    print(f"{x} - {y} = {x - y}")

def multiply(x, y):
    print(f"{x} * {y} = {x * y}")

def divide(x, y):
    try:
        print(f"{x} / {y} = {x / y}")
    except ZeroDivisionError:
        print("***\nThe sceond number should not be zero. Please try again.\n***")

instruction = 'a'

while instruction != 'q':
    printScreen()
    instruction = input("Input command (or input q to quit) >> ").lower()
    if instruction == 'q':
        break
    elif instruction in ['a', 'b', 'c', 'd']:
        values = getInputs()
        if values != None:
            x, y = values
            if instruction == 'a':
                add(x, y)
            elif instruction == 'b':
                subtract(x, y)
            elif instruction == 'c':
                multiply(x, y)
            elif instruction == 'd':
                divide(x, y)
        else:
            print("***\nThere are mmissing input. / There are too many inputs. / The inputs are not integers.\nPlease try again.\n***")
    else:
        print("***\nThere is no valid command. Please try again.\n***")
