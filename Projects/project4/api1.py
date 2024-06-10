# Project3 - API 1 Module.
# API Reference: https://github.com/wh-iterabb-it/meowfacts

import requests
import json

def catfacts():
    response = requests.get("https://meowfacts.herokuapp.com/")
    py_obj = json.loads(response.text)
    json_parsed = py_obj['data'][0]
    print(json_parsed)
