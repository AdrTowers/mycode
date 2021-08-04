#!/usr/bin/python

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# Function 1
for farm in farms:
    for agri in farm.get("agriculture"):
        print(" -",agri)


# Function 2
answer = input(f"Please select a Farm: {[x['name'] for x in farms]}\n>")
for farm in farms:
    if farm["name"].lower() == answer.lower():
        for agri in farm["agriculture"]:
            print(agri)
                

# Function 3
