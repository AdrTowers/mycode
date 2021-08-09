#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_HOUSE = "https://anapioficeandfire.com/api/houses/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #pprint.pprint(got_dj)
        name = got_dj['name']
        house = got_dj['allegiances']
        books = got_dj['books'] + got_dj['povBooks']
        
        print("Allegiances:")
        for link in house:
            print(requests.get(link).json()['name'])
        
        print("Books:")
        for link in books:
            print(requests.get(link).json()['name'])

        #houseresp = requests.get(house)
        #print(houseresp)
        #got_house = houseresp.json()

        #housename= got_house['name']

        #print(f"{name} belongs to {housename}")

if __name__ == "__main__":
        main()

