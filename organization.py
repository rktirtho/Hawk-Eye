import requests
import json

url = ""
api_request = requests.get(url)
api = json.loads(api_request.content)
