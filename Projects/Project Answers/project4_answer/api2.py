# Project3 - API 2 Module.
# API Reference: https://api-ninjas.com/api/cats

import requests
import json
import os
import pprint

from dotenv import load_dotenv
load_dotenv()
CAT_BREED_TOKEN = os.getenv("CAT_BREED_TOKEN")

def catbreed(breed):
    api_url = 'https://api.api-ninjas.com/v1/cats?name='+ breed
    response = requests.get(api_url, headers={'X-Api-Key': CAT_BREED_TOKEN})
    py_obj = json.loads(response.text)
    cat_breed = py_obj[0]['name']
    origin = py_obj[0]['origin']
    length = py_obj[0]['length']
    life = py_obj[0]['max_life_expectancy']
    min_weight = py_obj[0]['min_weight']
    max_weight = py_obj[0]['max_weight']
    return \
        pprint.pprint("Breed: " + cat_breed), \
        pprint.pprint("Origin: " + origin), \
        pprint.pprint("Length: " + length), \
        pprint.pprint("Weight: " + str(min_weight) + " to " + str(max_weight) + " lbs"), \
        pprint.pprint("Life Span: " + str(life) + " years")
