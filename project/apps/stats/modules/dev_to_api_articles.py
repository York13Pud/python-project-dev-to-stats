# --- Import the required libraries:
import json
import requests


def get_published_articles(api_key:str, api_endpoint: str):
    """Function:

    Makes an API call to dev.to which pulls the list of published articles for your account.
    
    Args:
        api_key (str): Your unique API key.
        api_endpoint (str): The URL for the API endpoint.

    Returns:
        response (Class): Returns the payload of the request in a JSON format.
    """
    
    headers = {"api-key": api_key,
               "Accept": "application/vnd.forem.api-v1+json"}

    # --- 
    params = {"per_page": 1000}
    
    # --- Endpoint is: https://dev.to/api/articles/me/published?per_page=1000
    URL = api_endpoint
    
    # --- Execute an API GET request to the API:
    
    response = requests.request("GET", url = URL, 
                            params = params, 
                            headers = headers)

    response_text = response.text
    
    response_data = json.loads(response_text)
    
    response_status_code = response.status_code

    return [response_data, response_status_code]


def get_followers(api_key:str, api_endpoint: str, page_number: int):
    """Function:

    Makes an API call to dev.to which pulls the list of published articles for your account.
    
    Args:
        api_key (str): Your unique API key.
        api_endpoint (str): The URL for the API endpoint.

    Returns:
        response (Class): Returns the payload of the request in a JSON format.
    """
    
    headers = {"api-key": api_key,
               "Accept": "application/vnd.forem.api-v1+json"}

    # --- 
    params = {"per_page": 1000,
              "page": page_number}
    
    # --- Endpoint is: https://dev.to/api/articles/me/published?per_page=1000
    URL = api_endpoint
    
    # --- Execute an API GET request to the API:
    
    response = requests.request("GET", url = URL, 
                            params = params, 
                            headers = headers)

    response_text = response.text
    
    response_data = json.loads(response_text)
    
    response_status_code = response.status_code

    return [response_data, response_status_code]
