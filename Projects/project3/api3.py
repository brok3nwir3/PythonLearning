# Project3 - API 3 Module.
# API Reference: 

import requests
import json
import os
import webbrowser

from dotenv import load_dotenv
load_dotenv()
CAT_IMAGE_TOKEN = os.getenv("CAT_IMAGE_TOKEN")

def catimage():
    response = requests.get("https://api.thecatapi.com/v1/images/search?api_key=" + CAT_IMAGE_TOKEN)
    py_obj = json.loads(response.text)
    json_parsed = py_obj[0]['url']
    webbrowser.open(json_parsed, new=0, autoraise=True)
    #print(json_parsed)

catimage()

# url = "https://cataas.com/cat/"
# url = "https://api.thecatapi.com/v1/images/search?api_key="
# cat_page = url + CAT_IMAGE_TOKEN
# webbrowser.open(cat_page, new=0, autoraise=True)