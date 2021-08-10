#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/rovers/"


# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "&api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    # request user input 
    rover = input("Which rover would you like to view? Curiosity, Opportunity, or Spirit\n").lower()
               
    earthdate = input("What earth date was it taken on? ex. yyyy-mm-dd\n")
    earthdate = "/photos?earth_date=" + earthdate
    
    ## make a call to NASAAPI with our key
    url= NASAAPI + rover +  earthdate + nasacreds

    print("Source url: " + url)

    apodresp= requests.get(url)


    ## strip off json
    apod = apodresp.json()

    #print(apod)
    if apod['photos'] == "":
        print("No available data")

    print()

    print("Rover: " + apod['photos'][0]['rover']['name'] + "\n")

    print("Date on Earth: " + apod['photos'][0]['earth_date'] + "\n")

    print("Image url: " + apod['photos'][0]['img_src'])

if __name__ == "__main__":
    main()
