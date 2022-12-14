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
    
    headers = {api_key_name: api_key_secret}

    params = {"per_page": 15}

    URL = "https://dev.to/api/articles/me/published"
    
    # --- Execute an API GET request to the API:
    logging.info(msg = f"Running {__name__} function")
    
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)
    
    if response.status_code == 200:
        logging.info(msg = f"{response.status_code} Connected to {URL} successfully")
        return response
    
    else:
        logging.error(msg = f"{response.status_code} {URL} {response.reason}")
        return response