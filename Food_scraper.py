import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the URL
url = "https://www.foodnetwork.com/recipes"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all recipe links on the page
recipe_links = soup.find_all("a", class_="o-ResultCard__a-Anchor")

# Extract information from each recipe link
for link in recipe_links:
    recipe_url = link["href"]
    recipe_name = link.find("h3", class_="m-MediaBlock__a-HeadlineText").get_text()
    recipe_cuisine = link.find("span", class="o-RecipeInfo__a-Category").get_text()

    # Print out the recipe name and URL
    print(recipe_name)
    print(recipe_url)
