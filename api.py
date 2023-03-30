import requests
import json
from dotenv import load_dotenv
load_dotenv()

import os
#update key
SUBSCRIPTION_KEY = os.environ.get('SUBSCRIPTION_KEY')

endpoint = 'https://python-image-analyzer-elub.cognitiveservices.azure.com/'
request_url = 'https://{endpoint}/vision/v3.2/analyze'

parameters = {'visualFeatures' : 'Description,Color','language' : 'en'}

image_path = './test_images/PolarBear.jpg'
image_data = open(image_path, "rb").read()

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
}

response = requests.post(request_url, headers=headers, params=parameters, data=image_data)

response.raise_for_status()

results = response.json()
print(json.dumps(results))
