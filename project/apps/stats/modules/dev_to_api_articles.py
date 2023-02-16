# --- Import the required libraries:
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

    params = {"per_page": 1000}
    
    # --- Endpoint is: https://dev.to/api/articles/me/published?per_page=1000
    URL = api_endpoint
    
    # --- Execute an API GET request to the API:
    
    response = requests.get(url = URL, 
                            params = params, 
                            headers = headers)

    response_json = response.json()
    response_status_code = response.status_code
    # print(response.status_code)
    #response_json["response"] = response.status_code
    
    return [response_json, response_status_code]
