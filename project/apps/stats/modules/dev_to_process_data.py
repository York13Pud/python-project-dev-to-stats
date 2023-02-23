# --- Import required modules and libraries:
from .db_functions import get_all_articles, add_article, get_all_tags, check_tag, add_article_comments_count, add_article_likes_count, add_article_views_count
from .dev_to_api_articles import get_published_articles
from ...users.models import User

import environ

def testing_function():   
    
    users = User.objects.values_list("id", "api_key", named=True)
    
    for user in users:
        if user.api_key != None:
    
            # --- Make API call to collect published articles:
            dev_to_api_key = user.api_key
            api_endpoint_url = "https://dev.to/api/articles/me/published"
            
            published_articles = get_published_articles(api_key = dev_to_api_key,
                                                        api_endpoint = api_endpoint_url)
            
            response_code = published_articles[1]
            published_articles = published_articles[0]
                                    
            
            # --- Check for a HTTP 200 response. If not 200, log and end process:
            if response_code != 200:
                # # # # Change to log entry and end
                print(f"Response code is {response_code}. It should be 200. Please check your API key is correct.")
            
            else:
            
                # --- Call function to query the articles table to collect all known articles:
                known_articles = get_all_articles()
                print(known_articles)
                
                # --- Query article ref ID against each article in API return:
                for published_article in published_articles:
                    if published_article["id"] in known_articles:
                        # # # # Change to log entry
                        print(f"Article {published_article['id']} is present")
                        article_id = 
                        # # --- Proceed to check views, comments and likes count
                        # add_article_views_count(article_id = str(published_article["id"]), 
                        #                         article_views = int(published_article["page_views_count"]))
                        # add_article_likes_count(article_id = str(published_article["id"]), 
                        #                         article_likes = int(published_article["public_reactions_count"]))
                        # add_article_comments_count(article_id = str(published_article["id"]), 
                        #                            article_comments = int(published_article["comments_count"]))
                        
                    else:
                        print(f"Article {published_article['id']} is not present")
                        # --- Get tags from list in article
                        tags_to_check = list(published_article['tag_list'])
                        
                        tag_check = check_tag(tags_to_check = tags_to_check)

                        # # --- Once tag check is completed, call function to query tags table to collect all tag names
                        # all_tags = get_all_tags()
                        # print(all_tags)
                        
                        # # --- and add article to articles table.
                        # add_article()
                        
                        # # --- Then add the tags / article to the article_tags table where needed: