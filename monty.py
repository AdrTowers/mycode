#!/usr/bin/python3
# try/except error handling
while True:
    try:
        print("Guess a number that cleanly divides 12!")
        num= int(input(">"))
        answer= 12 / num
        print(answer)
        break
    except ValueError as resp:
        print("That isn't a numeral!")
        print(resp)
    except ZeroDivisionError as resp:
        print("You can't divide by zero!")
        print(resp)
    except Exception as resp:
        print("I've never seen anyone screw up like THAT before!")
        print(resp)
