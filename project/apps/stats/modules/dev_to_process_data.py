# --- Import required modules and libraries:
from .db_functions import get_all_articles, add_article, get_all_tags, check_tag
from .dev_to_api_articles import get_published_articles

import environ

def testing_function():
    # --- Make API call to collect published articles:
    
    env = environ.Env(DEBUG=(bool, False))
    
    dev_to_api_key = env("DEV_TO_API_KEY")
    api_endpoint_url = "https://dev.to/api/articles/me/published"
    
    published_articles = get_published_articles(api_key = dev_to_api_key,
                                                api_endpoint = api_endpoint_url)

    
    response_code = published_articles[1]
    published_articles = published_articles[0]
    print(response_code)
       
    # --- Check for a HTTP 200 response. If not 200, log and end process:


    # --- Call function to query articles table to collect all articles:
    all_articles = get_all_articles()
    # print(all_articles)
    
    
    # --- Query article ref ID against each article in API return:
    for published_article in published_articles:
        print(f"Name: {published_article['title']}")
        if published_article["id"] in all_articles:
            print(f"Article {published_article['id']} is present")
        else:
            print(f"Article {published_article['id']} is not present")


    # --- Call function to check article tags:
    # tags_to_check = [{"name": "python"},
    #                  {"name": "javascript"},
    #                  {"name": "c#"},
    #                  {"name": "100daysofcode"},
    #                  {"name": "codenewbie"}]
    
    # tag_check = check_tag(tags_to_check = tags_to_check)
    # print(tag_check)

    # --- Once tag check is completed, call function to query tags table to collect all tag names
    # all_tags = get_all_tags()
    # print(all_tags)
    
    # --- and add article to articles table.
    # add_article()
    
    # --- Then add the tags / article to the article_tags table where needed: