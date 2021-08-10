#!/usr/bin/python3

import requests

API = "https://opentdb.com/api.php?amount=10&category=31&difficulty="

#end of endpoint
multi = "&type=multiple"

def main():

    diff = input("Select your difficulty. Easy, medium, or hard.\n").lower()

    # get request
    URL = API + diff + multi
   
    gettrivia = requests.get(URL)

    trivia = gettrivia.json()

    #print(trivia)

    multiquest = []

    for quest in trivia["results"]:
        print(quest['question'])

        multiquest = quest['correct_answer']
        multiquest.append(quest['incorrect_answers'])

if __name__ == "__main__":
    main()
