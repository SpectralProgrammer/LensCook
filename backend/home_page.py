# Importing required libraries
import streamlit as st
from PIL import Image
import urllib.request
from bs4 import BeautifulSoup

import imagedetect
from listrecipes import list_recipes
import cv2
import numpy as np

def printRecipes(recipes):
    for i, recipe in enumerate(recipes):
        st.write(f"**Recipe {i+1}: {recipe.title}**")
        st.write(f"{recipe.likes} likes")

        url = recipe.imageURL
        st.image(url)

        st.write("----")
        ing_used = ", ".join(ingredient for ingredient in recipe.ingredientsUsed)
        st.write(f"Ingredients Used: {ing_used}")
        ing_missing = ", ".join(ingredient for ingredient in recipe.ingredientsMissing)
        st.write(f"Ingredients Missing: {ing_missing}")
        st.write("----")
        soup = BeautifulSoup(recipe.summary)
        st.write(soup.get_text())
        # st.write(recipe.summary)

st.title("**LensCook** - Let's Cook Together.")
st.subheader("Seek | Cook | Savor")

with st.sidebar:
    st.title("LensCook")
    st.subheader("Your recipe curator.")
    st.write("LensCook is an application that allows users to upload a picture of their available ingredients and get back recipes that utilize them through the use of Google Cloud Vision and a recipes database.")

st.divider()

num_of_recipes = st.number_input("Number of recipes: ", min_value=1)
num_of_servings = st.slider("Servings: ", min_value=1, max_value=20)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    dish_types = st.radio("Select dish type: ", ["Breakfast", "Lunch", "Dinner"])
with col2:
    time_needed = st.radio("Cook times: ", ["Quick", "Normal", "Complex"])
with col3:
    price_choice = st.radio("Preparation price: ", ["Cheap", "Expensive"])
with col4:
    recipe_preferences = st.radio("Dietary Restrictions: ", ["None", "Vegan", "Vegetarian", "Dairy Free", "Gluten Free"])
with col5: 
    allergens_control = st.multiselect("Select Any Allergens / No-Gos: ", ["Peanuts", "Lactose", "Fish", "Wheat"])

pic_choice = st.radio("Which one do you want to use?", ["Camera to take Image", "Upload Image"])

if pic_choice == "Camera to take Image":
    ingredients_pic = st.camera_input("Snap a pic of your ingredients!")
else:
    ingredients_pic = st.file_uploader("Upload Image")

if ingredients_pic is not None:
    im1 = Image.open(ingredients_pic)
    saved_path = "ingredients.jpg"
    im1.save(saved_path)

    ingredients = imagedetect.find_ingredients(path=saved_path)

    print("Ingredients found in image: " + str(ingredients))

    ranking = 2 # reduce missing ingredients   
    limit_license = "true"
    ignore_pantry = "false"

    detected_ing = ingredients
    d_ings=", ".join(ing for ing in detected_ing)

    st.write(f"Detected ingredients: {d_ings}")
    modify_choice = st.radio("Do you want to modify the detected ingredients?", ["no", "yes"])

    if modify_choice == "yes":
        new_ing = st.text_input("Type updated ingredients list (separated by commas)", d_ings)
        if new_ing:
            ingredients = [ing.strip() for ing in new_ing.split(",")]
        st.write(f"Updated ingredients: {', '.join(ingredients)}")

    confirm = st.button("Confirm Choices and start curating recipes")

    if confirm:
        print(d_ings)
        recipes = list(set(list_recipes(ingredients, num_of_recipes, ranking, limit_license, ignore_pantry)))

        ingredients_found = False

        if recipes:
            ingredients_found = True
            recipes.sort(key= lambda x: x.likes, reverse=True)

            printRecipes(recipes)
        else:
            ingredients_found = False
            print("No recipes / ingredients found.")
else:
    st.write("")