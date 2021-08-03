#!/usr/bin/python3
import random

turns = 10
guess_num = 0
user_input = int(input("Pick a number between 1 and 100"))
rand_num = random.randint(1, 100)
while user_input != rand_num and turns != 0:
    guess_num += 1
    turns -= 1
    if user_input < rand_num:
        print("Too low")
    if user_input > rand_num:
        print("Too high")

    user_input = int(input("Pick another number between 1 and 100"))
if turns != 0:
    print("Congrats! You picked the right number!!! It took you " + str(guess_num) + " tries")
else:
    print("Sorry, you lost. The correct answer is", str(rand_num))
