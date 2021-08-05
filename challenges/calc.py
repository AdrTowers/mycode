#!/usr/bin/env python3
def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def divide(x, y):
    print(x / y)

def multiply(x, y):
    print(x * y)

def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER  number: "))
            break
        except:
            print("Invalid input, try again.")

    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    if(operation == "add"):
        add(x, y)
    elif(operation == "subtract"):
        subtract(x, y)
    elif(operation == "divide"):
        if y != 0:
            divide(x, y)
        else:
            print("You can't divide by zero!")
    elif(operation == "multiply"):
        multiply(x, y)
    else:
        print("use a valid OPTION")

if __name__ == "__main__":
    main()
