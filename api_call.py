# --- Import the required libraries:
import requests
import logging

def api_call(api_key_name:str, api_key_secret:str):
    """Function:

    Makes an API call to dev.to which pulls the list of published articles for your account.
    
    Args:
        api_key_name (str): The name of the API key for the API request. For dev.to, this is normally called api-key.
        api_key_secret (str): Your unique API key.

    Returns:
        response (Class): Returns the payload of the request in a JSON format.
    """
    
    log_file = "logs/api-call-log.log"
    
    logging.basicConfig(filename = log_file, 
                        encoding = "utf-8", 
                        level = logging.INFO,
                        format='%(levelname)s:%(asctime)s:%(message)s')
    
    headers = {api_key_name: api_key_secret}

    params = {"per_page": 15}

    URL = "https://dev.to/api/articles/me/publishe"


    # --- Execute an API GET request to the API:
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)
    
    if response.status_code == 200:
        logging.info(msg = f"{response.status_code} Connected to {URL} successfully")
        return response
    
    else:
        logging.error(msg = f"{response.status_code} {response.reason}")
        msg = "Error. Please see log file"
        return response
    

def create_dataframe():
    # --- Convert the json response to a pandas dataframe:
    df = convert_json_to_df(response=response)


    # --- Show the dataframes contents:
    print(df.head(n = 3))