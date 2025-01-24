# Importing requires libraries
import requests
import json
from typing import List

from Recipe import Recipe

def list_recipes(ingredients, num_of_recipes, ranking, limit_license, ignore_pantry, allergens=None) -> List[Recipe]:
  """
  Returns a list of Recipe objects (see Recipe.py)
  """
  # Make secret when transfer to VS Code
  api_key = "785a8ee07e814bfb9e1e4062897c3030"
  
  url = "https://api.spoonacular.com/recipes/findByIngredients"


  # while num_recipes_generated < num_of_recipes:    
    # To add parameter, add the following: "&parameter=value"
  query_params = f"apiKey={api_key}&ingredients={ingredients}&number={num_of_recipes + 2}"
  
  query = url + "?" + query_params

  # json
  response = requests.get(query).json()

  print("Ingredients Passed:", ingredients)
  print("Recipes Found:", response)

  recipes = []
  recipecount = 0

  for recipe in response:
    newrecipe = Recipe(
        id=recipe["id"],
        title=recipe["title"],
        imageURL=recipe["image"],
        likes=recipe["likes"],
        ingredientsUsed=[ingredient["name"] for ingredient in recipe["usedIngredients"]],
        ingredientsUnused=[ingredient["name"] for ingredient in recipe["unusedIngredients"]],
        ingredientsMissing=[ingredient["name"] for ingredient in recipe["missedIngredients"]]
      )
    
    if allergens != None:
      allercount = 0
      for ingredient in recipe["usedIngredients"]:
        if ingredient in allergens: 
          allercount += 1
      if allercount == 0:
          recipes.append(newrecipe)
          recipecount += 1
    else:
      recipes.append(newrecipe)
      recipecount += 1

    if recipecount >= num_of_recipes:
      return recipes

  return recipes  # Ensure a list is always returned
