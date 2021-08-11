#!/usr/bin/python3
  
import csv

# open data file and loop through it
with open("pokedex.txt", "r") as pokefile:
    reader = csv.reader(pokefile)
    
    i = 0
    max = 200
    for row in reader:
        i += 1

        print(row)
