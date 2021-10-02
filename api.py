import base64
import requests
from flask import Flask

# encode image to base64
image = request.form.get('output')
with open(image, "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

your_api_key = "ZsHWC9k99JNTJOL1Ie6qBu9EzEUx3KPTWC0Sxltgzyc5mKMQZ0"
json_data = {
    "images": images,
    "modifiers": ["similar_images"],
    "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
}

response = requests.post(
    "https://api.plant.id/v2/identify",
    json=json_data,
    headers={
        "Content-Type": "application/json",
        "Api-Key": your_api_key
    }).json()

for suggestion in response["suggestions"]:
    print(suggestion["plant_name"])    # Taraxacum officinale
    print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
    print(suggestion["plant_details"]["url"])