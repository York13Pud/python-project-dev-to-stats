# --- Import the required libraries:
from urllib import request
import pandas as pd


def convert_json_to_df(response:list):
    """Function:
    
    Converts a JSON response to a pandas dataframe, drop unused columns and convert published_at to datetime.

    Args:
        response (list): The response of the api call.

    Returns:
        df (Dataframe): A pandas dataframe with all of the published articles for the account
    """
    
    df = pd.json_normalize(response.json())
    
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

    df["published_timestamp"] = pd.to_datetime(df["published_timestamp"], 
                                               utc = False)
    
    return df