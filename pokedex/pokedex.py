#!/usr/bin/env python3

import csv

# open data file and loop through it
with open("pokedex.txt", "r") as pokefile:
    # counter to create unique file names
    i = 0
    # loop across our open file line by line
    for row in csv.reader(pokefile):
        i = i + 1  # increase i by 1 (to create unique admin.rc file names)
        # this f string says "fill in the value of i"
        filename = f"poke.txt{i}"

        # open a file via "with". This file will autoclose when the indentations stop
        with open(filename, "w") as pokemonfile:
            print("This is a test of my file" + row[0], file=pokemonfile)

# Display when the looping is complete
print("File has been created!")    
