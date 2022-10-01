# --- Import the required libraries:
import os
import pandas as pd
import requests


# --- Set the variables needed for the API call:L:
api_key_name = "api-key"
api_key_secret = os.getenv("DEVTO")

headers = {api_key_name: api_key_secret}

params = {"per_page": 2}

url = "https://dev.to/api/articles/me/published"


# --- Execute an API GET request to the API:
response = requests.get(url = url, 
                        params = params, 
                        headers = headers)


# --- Convert the response to a pandas dataframe:
df = pd.json_normalize(response.json())


# --- Show the dataframes contents:
print(df)