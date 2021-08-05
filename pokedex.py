#!/usr/bin/env python3

import pandas as pd

# Define the name of our xls file
poke_file= "pokedex.txt"

# Reading in a spreadsheet?
#pokedex = pd.read_excel(excel_file, sheet_name=0, index_col=0)

#pokedex2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)

# Reading in a csv file?
#pokedex = pd.read_csv(excel_file)

with open("pokedex.txt", "r") as comicfile:
    
