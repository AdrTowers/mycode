#!/usr/bin/python3
import requests
import random

# an inventory, which is initially empty
inventory = []
# start the player in the Hall
currentRoom = 'Entrance'

# possible directions
directions = []
all_directions = ["north", "east", "south", "west"]

killedMonster = False

CAT_API_URL = 'https://catfact.ninja/facts?limit=3&max_length=88'

# a dictionary linking a room to other rooms
rooms = {
    'Entrance': {
        'east': 'Hall', # need key to get in Hall
        'item': ['key'] 
    },
    'Hall': {
        'south': 'Kitchen',
        'north': 'Deck',
        'east': 'Dining Room',
        'west': 'Entrance',
    },
    'Deck': {
        'south': 'Hall',
        'item': ['sword'] # need sword to kill monster
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden', 
        'item': ['potion'],
        'north': 'Pantry',
        'east': 'Vault Room'
    },
    'Garden': {
        'north': 'Dining Room',
        'item': 'cat'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': ['IED']
    },
    'Vault Room': {   # need code to get in random guess up to 3
        'south': 'Garage',
        'item': ['$$$', 'gold', 'passport']
    },
    'Garage': {
        'north': 'Vault Room',
        'item': 'lamborghini',  # in lambo
        'east': 'Street'  # WIN scenario
    },
    'Street': {
        'west': 'Garage'
    }
}


# Replace RPG starter project with this code when new instructions are live
def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)

    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + str(rooms[currentRoom]['item']))
    # print random CAT FACTs from API when the player sees cat in the Garden
    if currentRoom == "Garden":
        print("You yelled at the cat. The cat throws random CAT-FACTS below:\n")
        getCatFacts()
            
    # print the current inventory
    print("---------------------------")
    print('Inventory : ' + str(inventory))

    # print possible directions in a room
    for key in rooms[currentRoom].keys():
        if key in all_directions:
            directions.append(key)
    print(f"Where do you wanna go?{directions}")

# get random cat-facts from cat fact API
def getCatFacts():
    response = requests.get(CAT_API_URL)
    catFacts = response.json().get("data")
    for fact in catFacts:
        print(fact["fact"])


showInstructions()

# loop forever
while True:
    showStatus()
    directions.clear()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>> ')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they have key to get in through the entrance
        if currentRoom == "Entrance" and move[1] in rooms[currentRoom]:
            if 'key' in inventory:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("You need to get KEY to get in. DUHH!!!!")
        elif currentRoom == "Dining Room" and move[1] == "east" and move[1] in rooms[currentRoom]:
        # player needs to guess code to get into vault room. Code a random number between 1-5
            random_code = str(random.randint(1,5))
            vault_code = ""
            while vault_code != random_code:
                vaultCode = input("You are entering a vault room. \nEnter code to get inside the vault room: [* HINT: single num between 1-5]\n>>")
                if random_code == vaultCode:
                 # set the current room to the new room
                    print("Correct code entered")
                    currentRoom = rooms[currentRoom][move[1]]
                    break
                print("Incorrect code entered. Try again..")
        elif move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'kill'
    if move[0] == 'kill':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            if 'sword' in inventory:
                if rooms[currentRoom]['item'] == "monster":
                    killedMonster = True
                    del rooms[currentRoom]['item']
                    print("Great Work!! You killed the MONSTER !!!!")
            else: 
                print("You don't have sword in inventory to kill the", rooms[currentRoom]['item'])

    # SUPER-WIN scenario
    if killedMonster == True and '$$$' in inventory and 'lamborghini' in inventory and currentRoom == 'Street':
        print(f'YOU SUPER WIN! You KILLED the monster and escaped the house with {inventory}')
        break
    # WIN scenario
    elif '$$$' in inventory and 'lamborghini' in inventory and currentRoom == 'Street':
        print(f'YOU WIN! You escaped the house with {inventory}')
        break
    # If a player enters a room with IED, LOSES
    elif 'item' in rooms[currentRoom] and 'IED' in rooms[currentRoom]['item']:
        print("IED Exploded. YOU ARE DEAD!!!!!")
        break
    elif currentRoom == 'Street':
        print("YOU JUST SURVIVED THE MONSTER. Consoloation WIN only!!!")
        break

