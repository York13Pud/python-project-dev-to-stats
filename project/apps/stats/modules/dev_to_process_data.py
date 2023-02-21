# --- Import required modules and libraries:
from .db_functions import get_all_articles, add_article, get_all_tags, check_tag

def testing_function():
    # --- Make API call to collect published articles:


    # --- Check for a HTTP 200 response. If not 200, log and end process:


    # --- Call function to query articles table to collect all articles:
    all_articles = get_all_articles()
    
    print(all_articles)
    
    # --- Query article ref ID against each article in API JSON / Pandas return:


    # --- Call function to check article tags:
    tags_to_check = [{"name": "python"},
                     {"name": "javascript"},
                     {"name": "c#"},
                     {"name": "100daysofcode"},
                     {"name": "codenewbie"}]
    
    tag_check = check_tag(tags_to_check = tags_to_check)
    print(tag_check)

    # --- Once tag check is completed, call function to query tags table to collect all tag names
    all_tags = get_all_tags()
    print(all_tags)
    
    # --- and add article to articles table.
    add_article()
    
    # --- Then add the tags / article to the article_tags table where needed: