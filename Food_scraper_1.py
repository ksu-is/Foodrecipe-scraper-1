import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

while True:
    # Prompt user to input name
    recipe_name = input("Enter a recipe name: ")

    # Construct URL with a search query
    encoded_recipe_name = quote(recipe_name)
    url = f"https://www.foodnetwork.com/search/{encoded_recipe_name}-"
    response = requests.get(url, timeout=5)

    # Parse the HTML content using Beautiful soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first search result link
    search_result = soup.find("h3", class_="m-MediaBlock__a-Headline")

    if search_result is None:
        print("No results found. Please try again.")
        continue

    # Extract the recipe URL from the search result link
    recipe_tag = search_result.a
    recipe_url = "https:" + recipe_tag['href']

    # Send an HTTP request to the recipe URL
    response = requests.get(recipe_url, timeout=5)

    # Parse the HTML Content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find recipe name
    recipe_name = soup.find("span", class_="o-AssetTitle__a-HeadlineText").contents

    # Find the ingredients list and process
    ingredients_list = soup.find("div", class_="o-Ingredients__m-Body")
    process_list = soup.find_all("li", class_="o-Method__m-Step")

    print(f"Recipe: {recipe_name}")
    print("Ingredients")
    for ingredient in ingredients_list:
        print(ingredient.get_text())

    print("\nProcess: ")
    for step in process_list:
        print(step.get_text())

    # Ask user if they want to search for another recipe
    while True:
        user_choice = input("Do you want to search for another recipe? (y/n): ")
        if user_choice in ["y", "n"]:
            break
        print("This choice is not available. Please try again.")
    if user_choice == "y":
        continue
    else:
        print("Thank you for using the tool. Goodbye!")
        break