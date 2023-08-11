# --- Import required modules and libraries:
from .db_functions import get_all_articles, add_article, \
                          get_all_tags, check_tag, \
                          add_article_comments_count, add_article_likes_count, add_article_views_count, \
                          get_last_follower_count, add_followers_count
                          
from .dev_to_api_articles import get_published_articles, get_followers
from ...users.models import User


def process_data():   
    
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
                
                
                # # --- Query article ref ID against each article in API return: 
                for published_article in published_articles:
                    if published_article["id"] in known_articles:
                        # # # # Change to log entry
                        print(f"Article {published_article['id']} is present.")
                        
                        # --- Proceed to check views, comments and likes count
                        add_article_views_count(article_ref_id = int(published_article["id"]), 
                                                article_views = int(published_article["page_views_count"]))
                        add_article_likes_count(article_ref_id = int(published_article["id"]), 
                                                article_likes = int(published_article["public_reactions_count"]))
                        add_article_comments_count(article_ref_id = int(published_article["id"]), 
                                                   article_comments = int(published_article["comments_count"]))
                        
                    else:
                        print(f"Article {published_article['id']} is not present")
                        
                        # --- Get tags from list in article:
                        tags_to_check = list(published_article['tag_list'])
                        
                        check_tag(tags_to_check = tags_to_check)
                        
                        # # --- Finally, call the add article to articles table.
                        add_article(article = published_article, user_id = user.id)
                        

def process_followers_data():   
    
    users = User.objects.values_list("id", "api_key", named=True)
        
    for user in users:
        
        if user.api_key != None:
           
            page_number = 1
            end_of_pages = False
            follower_count = 0

            while end_of_pages == False:
                # --- Make API call to collect followers:
                dev_to_api_key = user.api_key
                api_endpoint_url = "https://dev.to/api/followers/users"
                
                followers = get_followers(api_key = dev_to_api_key,
                                          api_endpoint = api_endpoint_url,
                                          page_number=page_number)
                
                response_code = followers[1]
                followers = followers[0]
                               
                # --- Check for a HTTP 200 response. If not 200, log and end process:
                if response_code != 200:
                    # # # # Change to log entry and end
                    print(f"Response code is {response_code}. It should be 200. Please check your API key is correct.")
                    end_of_pages = True
                    
                else:
                    # --- Call function to query the articles table to collect all known articles:
                    followers_on_page = len(followers)
                                        
                    if followers_on_page == 0:
                        # --- Process new entry into database:
        
                        # --- 1. Get the last record from Followers table model for the current user:
                        current_follower_count = get_last_follower_count(user_id = user.id)
                        
                        # --- Work out the difference between the current_follower count
                        # --- and the follower_count
                        print(type(follower_count))
                        print(type(current_follower_count))
                        follower_count_difference = follower_count - current_follower_count
                        
                        print(current_follower_count)
                        
                        # --- Add entry to the Followers table:
                        print("writing record ....")
                        add_followers_count(user_id = int(user.id), 
                                            change = follower_count_difference,
                                            count = follower_count)
                        
                        # --- Set end_of_pages to True to break the while loop:
                        end_of_pages = True
                    
                    else:
                        follower_count += followers_on_page
                        page_number += 1
        
        
        