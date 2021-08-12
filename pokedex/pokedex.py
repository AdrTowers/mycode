#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # import our file
    csv_file = 'pokedex.txt'

    # store pokedex data
    pokedex1 = pd.read_csv(csv_file, index_col=0)
    # DF has 5 rows and 13 columns
    print("First 20 pokemon\n", pokedex1.head(20))

    # sort by the pokemon Type 1
    sorted_by_Type1 = pokedex1.sort_values(["Type 1"], ascending=False)

    # Sort by the pokemon Name
    sorted_by_name = pokedex1.sort_values(["Name"], ascending=True)

    # Data is sorted by values in a column
    print("Sorted by Type 1\n", sorted_by_Type1.head(20))
    print("Sorted by Name\n", sorted_by_name.head(10))

    # Created smaller list of columns for the last twenty rows
    slimlist = pokedex1[["Name", "Type 1", "Type 2", "Generation"]]

    print(slimlist.tail(20))

    # Save to new files
    sorted_by_Type1.head(20).to_csv("typehead.csv")
    sorted_by_name.tail(20).to_csv("nametwenty.csv")
    slimlist.tail(50).to_csv("slimpokedex.csv")


if __name__ == "__main__":
    main()
