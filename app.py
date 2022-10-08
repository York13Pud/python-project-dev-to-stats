# --- Import the required libraries and modules:
import logging
import os
from api_call import api_call
from convert_json import convert_json_to_df

log_file = "logs/app.log"

logging.basicConfig(filename = log_file, 
                    encoding = "utf-8", 
                    level = logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

def main():
    logging.info(msg = "Starting application")
    
    # --- Set the required constants and variables
    API_KEY_NAME = "api-key"
    api_key_secret = os.getenv("DEVTO")

    # --- Make a call to the dev.io API for a users published articles:
    response = api_call(api_key_name =  API_KEY_NAME,
                        api_key_secret= api_key_secret)

    # print(response.content)

    if response.status_code == 200:
        # --- Convert the json response to a pandas dataframe:
        df = convert_json_to_df(response=response)

        # --- Show the dataframes contents:
        print(df.head(n = 3))

    else:
        print(f"Error: {response.status_code}: {response.reason}")
    
    logging.info(msg = "Stopping application")
    
# --- TO DO: Check HTTP response code and if 200, goto convert JSON. Otherwise error.

if __name__ == "__main__":
    main()