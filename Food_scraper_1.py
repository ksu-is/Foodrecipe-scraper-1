'''
This is a scraping tool, intended to help people decide and cook what's for dinner
'''

import requests
from bs4 import BeautifulSoup

while True: 
    # Prompt user to input name 
    recipe_name = input("Ente a recipe name: ")
    
    # Construct URL witha search query
    url = f"https://www.foodnetwork.com/search/{recipe_name}-CUSTOM_FACET:RECIPE_FACET"
    response = requests.get(url)
    
    #Parse the HTML content using Beautiful soup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the first search result link
    search_result = soup.find("a", class_="m-MediaBlock_a-headlineAnchor")

    if search_result is None:
        print("No results found. Please try again.")
        continue
    
