#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests


def main():
    
    # Ask the user for input in order to submit request
    user_link = input("Enter the wikipedia url of the movie you wish to find out more about.\n")

    # Use requests to load content url
    url = requests.get(user_link)
    print(url)

    # implement BeautifulSoup to convert content into a bs object
    soup = BeautifulSoup(url.content, "html.parser")

    # # Print contents using prettify to get a better structured object
    # contents = soup.prettify()
    # print(contents)

    # Infosection stores all of the right hand side information found on the wiki page
    infosection = soup.find(class_="infobox vevent")
    # print(infobox.prettify())

    # Rows will store the data for each tr tag inside of our infobox
    rows = infosection.find_all("tr")
    for row in rows:
        infobox = row.find("th", class_="infobox-label")
        infobox_values = row.find("td", class_="infobox-data")

        # if infobox is not None:
        #     # info_label = infobox.get_text()
        #     # infobox_data = infobox_values.get_text()

        print(f"""
        {infobox}: {infobox_values}
        """)


if __name__ == '__main__':
    main()
