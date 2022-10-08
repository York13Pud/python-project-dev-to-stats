# --- Import the required libraries and modules:
import os
from api_call import api_call
from convert_json import convert_json_to_df


# --- Set the required constants and variables
API_KEY_NAME = "api-key"
api_key_secret = os.getenv("DEVTO")

# --- Make a call to the dev.io API for a users published articles:
response = api_call(api_key_name =  API_KEY_NAME,
                    api_key_secret= api_key_secret)

print(response.content)
# --- TO DO: Check HTTP response code and if 200, goto convert JSON. Otherwise error.