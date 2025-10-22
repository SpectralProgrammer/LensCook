import os
from google.cloud import vision
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import requests
import json

# I love coding - Komal Jan 20th 2024 at 2:42 AM 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"
api_key = "785a8ee07e814bfb9e1e4062897c3030"

def find_ingredients(path):
    """Use Google Vision AI to Localize objects in the local image and draw 
       bounding polygons with labels.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    ingredients = client.object_localization(image=image, max_results=100).localized_object_annotations
    new_ing_names = []
    for i, ingredient in enumerate(ingredients):
        img = Image.open(path)
        width, height = img.size
        vx = []
        vy = []
        for vertex in ingredient.bounding_poly.normalized_vertices:
            vx.append([vertex.x * width])
            vy.append([vertex.y * height])
        left = min(vx)
        right = max(vx)
        top = min(vy)
        bottom = max(vy)
        dims = (left[0],top[0], right[0], bottom[0])
        im = img.crop(dims)
        name = "segments/segment" + str(i) + ".jpg"
        im = im.save(name)
        with open(name, "rb") as image_file:
            content = image_file.read()
        im = vision.Image(content=content)
        newings = client.object_localization(image=im, max_results=100).localized_object_annotations
        for ing in newings:
            if ing.name not in ["Vegetable", "Baked Goods", "Packaged Goods", "Food"]:
                new_ing_names.append(ing.name)
    # ingredients = []
    # for segment in segments:
    #     ingredients = client.object_localization(image=segment, max_results=100).localized_object_annotations
    # print(ingredients)
    # ingNames = [ingredient.name for ingredient in ingredients if ingredient.name != "Vegetable" and ingredient.name != "Food" and ingredient.name != "Packaged Goods"]
    return new_ing_names

if __name__ == "__main__":
    find_ingredients("uploads/ouiouibaguette.png")
