import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

while True:
    # Prompt user to input name
    recipe_name = input("Enter a recipe name: ")

    # Construct URL with a search query
    encoded_recipe_name = quote(recipe_name)
    url = f"https://www.foodnetwork.com/search/{encoded_recipe_name}-CUSTOM_FACET:RECIPE_FACET"
    response = requests.get(url)

    # Parse the HTML content using Beautiful soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first search result link
    search_result = soup.find("a", class_="m-MediaBlock_a-headlineAnchor")

    if search_result is None:
        print("No results found. Please try again.")
        continue

    # Extract the recipe URL from the search result link
    recipe_url = search_result["href"]

    # Send an HTTP request to the recipe URL
    response = requests.get(recipe_url)

    # Parse the HTML Content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find recipe name
    recipe_name = soup.find("h1", class_="o-AssetTitle__a-HeadlineText").get_text()

    # Find the ingredients list and process
    ingredients_list = soup.find_all("span", class_="ingredients-item-name")
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
        print("Invalid choice. Please try again.")
    if user_choice == "y":
        continue
    else:
        print("Thank you for using the tool. Goodbye!")
        break
    