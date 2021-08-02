#!/usr/bin/env python3
user_input = input("What is your name?")
user_input2 = input("What day of the week is it?")
## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("Hello", user_input, "!", "Happy", user_input2, "!", sep=" ")
