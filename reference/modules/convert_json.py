# --- Import the required libraries:
import logging
import pandas as pd


def convert_json_to_df(response:list):
    """Function:
    
    Converts a JSON response to a pandas dataframe, drop unused columns and convert published_at to datetime.

    Args:
        response (list): The response of the api call.

    Returns:
        df (Dataframe): A pandas dataframe with all of the published articles for the account
    """
    
    logging.info(msg = f"Running {__name__} function")
    
    logging.info(msg = f"Creating df Pandas Dataframe")    
    df = pd.json_normalize(response.json())
    
    logging.info(msg = f"Dropping unused columns from df Dataframe")  
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

    logging.info(msg = f"Converting 'published_timestamp' to datetime64")  
    df["published_timestamp"] = pd.to_datetime(df["published_timestamp"], 
                                               utc = False)
    
    return df