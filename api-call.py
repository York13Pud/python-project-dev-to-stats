# --- Import the required libraries:
import os
import pandas as pd
import requests


# --- Set the constants and variables needed for the API call:L:
API_KEY_NAME = "api-key"
api_key_secret = os.getenv("DEVTO")

headers = {API_KEY_NAME: api_key_secret}

params = {"per_page": 15}

URL = "https://dev.to/api/articles/me/published"


# --- Execute an API GET request to the API:
response = requests.get(url = URL, 
                        params = params, 
                        headers = headers)


# --- Convert the response to a pandas dataframe, drop unused columns and convert published_at to datetime:
df = pd.json_normalize(response.json())
df.drop(["type_of",
         "description", 
         "slug",
         "path",
         "body_markdown",
         "cover_image",
         "canonical_url",
         "reading_time_minutes",
         "positive_reactions_count",
         "published_at",
         "user.name",
         "user.username",
         "user.twitter_username",
         "user.github_username",
         "user.user_id",
         "user.website_url",
         "user.profile_image",
         "user.profile_image_90"], 
        axis = 1,
        inplace = True)

print(df.head(n = 3))

df["published_timestamp"] = pd.to_datetime(df["published_timestamp"], utc = False)

# --- Show the dataframes contents:
print(df.dtypes)
print(df.head(n = 3))