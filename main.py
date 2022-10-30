# --- Import the required libraries and modules:
import logging
import os
from api_call import api_call
from convert_json import convert_json_to_df


# --- Get the root folder path that the app is stored in:
APP_FOLDER_PATH = os.path.dirname(__file__)


# --- Setup the logging:
log_file = f"{APP_FOLDER_PATH}/logs/app.log"

logging.basicConfig(filename = log_file, 
                    encoding = "utf-8", 
                    level = logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')


# --- The main application:
def main():
    """
    _summary_
        This is the main application starting point.
    """
    
    logging.info(msg = "===== Starting application =====")
    
    # --- Set the required constants and variables
    API_KEY_NAME = "api-key"
    api_key_secret = os.getenv("DEVTO")

    # --- Make a call to the dev.io API for a users published articles:
    response = api_call(api_key_name =  API_KEY_NAME,
                        api_key_secret= api_key_secret)

    # --- Check the status code of the response and action accordingly:
    if response.status_code == 200:
        
        # --- Convert the json response to a pandas dataframe:
        df = convert_json_to_df(response=response)

        # --- Show the dataframes contents:
        print(df.head(n = 3))
        print(df.info())
        
    else:
        print(f"Error: {response.status_code}: {response.reason}")
    
    logging.info(msg = "===== Stopping application =====")


# --- Start the program if the name is "__main__":
if __name__ == "__main__":
    main()