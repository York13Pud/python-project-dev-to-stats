# --- Import the required libraries:
import requests


def get_user_details(api_key:str, api_endpoint:str):
    """Function:

    Makes an API call to dev.to which pulls the list of published articles for your account.
    
    Args:
        api_key (str): Your unique API key.

    Returns:
        response (Class): Returns the payload of the request in a JSON format.
    """
    
    headers = {"api-key": api_key,
               "Accept": "application/vnd.forem.api-v1+json"}

    params = {}

    URL = api_endpoint
    
    # --- Execute an API GET request to the API:
    
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)

    response_json = response.json()
    response_json["response"] = response.status_code
    
    return response_json


def get_published_articles(api_key:str):
    """Function:

    Makes an API call to dev.to which pulls the list of published articles for your account.
    
    Args:
        api_key (str): Your unique API key.

    Returns:
        response (Class): Returns the payload of the request in a JSON format.
    """
    
    headers = {"api-key": api_key,
               "Accept": "application/vnd.forem.api-v1+json"}

    params = {}

    URL = "https://dev.to/api/articles/me/published"
    
    # --- Execute an API GET request to the API:
    #logging.info(msg = f"Running {__name__} function")
    
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)
    
    if response.status_code == 200:
        #logging.info(msg = f"{response.status_code} Connected to {URL} successfully")
        print(response)
        return response
    
    else:
        #logging.error(msg = f"{response.status_code} {URL} {response.reason}")
        print(response)
        return response