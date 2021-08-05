#!/usr/bin/python3
from questions import questions

print("""
        *--------------------------------*
        | Harry Potter: Sorting Hat Quiz |
        |   Which house will you be in?  |
        *--------------------------------*
""")

turns = 0 # Keep track of turns as the game progresses

# Scores will house the number of times a particular answer is made
scores= {
         "gryffindor": 0,
         "hufflepuff": 0,
         "ravenclaw": 0,
         "slytherin": 0
         }
index = -1

while turns < 12:
    for quest in questions:
        index += 1
        turns += 1
        # Each question is pulled from an external dictionary
        userinput = input(print(questions[index]["question"])).title()
        if userinput == "A":
            scores["gryffindor"] += 1
        elif userinput == "B":
            scores["hufflepuff"] += 1
        elif userinput == "C":
            scores["ravenclaw"] += 1
        elif userinput == "D":
            scores["slytherin"] += 1
        elif userinput == "Quit":
            exit()     

if turns == 12:
    print("Congrats!! The house you belong to is....", max(scores, key=scores.get),"!!!")
# if userinput != "A" or "B" or "C" or "D" or "Quit":
#     print("You must choose either A, B, C, D or quit.")
