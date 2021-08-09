#!/usr/bin/python3
import requests

def main():
    """Run time code"""
    URL = "http://api.open-notify.org/iss-now.json"
    # Internation Space Station location api
    resp = requests.get(URL).json()

    # Store the results
    time= resp["timestamp"]
    lat= resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"] 
   
    # Display the results
    print(f"""
    The current location of the ISS
    Time: {time}
    Lat: {lat}
    Lon: {lon}
    """)
    

if __name__ == "__main__":
    main()
