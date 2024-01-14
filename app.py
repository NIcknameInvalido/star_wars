import requests as req
import pandas as pd

dataFromApi = req.get('https://swapi.dev/api/people')
json_data = dataFromApi.json()

df = pd.json_normalize(json_data, 'results')


print(df)