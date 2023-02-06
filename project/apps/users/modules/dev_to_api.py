# --- Import the required libraries:
import requests
import json

def get_user_details(api_key:str):
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

    URL = "https://dev.to/api/users/me"
    
    # --- Execute an API GET request to the API:
    
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)
    
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    
    else:
        print(response.content)
        # --- Add a redirect to an appropriate page
        return response


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