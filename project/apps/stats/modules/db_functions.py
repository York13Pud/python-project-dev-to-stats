# --- Import required modules and libraries:
from inspect import stack


from ..models import Articles, ArticleComments, ArticleLikes, ArticleViews, Tags


def get_all_tags():
    """_summary_
    Collects all of the tags from the tags table.
    
    Returns:
        list: all tags in the tags table.
    """
    
    try:
        # --- Get all of the tag names:
        all_tags = Tags.objects.values_list('name', flat = True)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return error_message
    
    else:
        return all_tags
    
    
def add_tag(tag_to_add: str):
    """_summary_
    This function will take the name of a tag and add it to the Tags table in the database.
    
    Args:
        tag_to_add (str): The tag that needs to be added.

    Returns:
        String: Either an error is returned or an added tag message is returned.
    """
    
    try:    
        # --- Add a tag to the tags table:
        Tags.objects.create(name = tag_to_add)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return error_message
    
    else:    
        # # # # Change this to a log entry:
        return f"Added tag {tag_to_add}"


def check_tag(tags_to_check: list):
    """_summary_
    This function will take a list of tags from an article and search through a 
    list of tags that are currently stored in the Tags table. 
    
    If the tag is found in the table, it will go onto the next tag, otherwise it
    will be added to the table.
    
    Args:
        tags_to_check (list): A list of tags that are taken from an article to check.
        current_tags (list): A list of tags that are currently stored in the Tags table.

    Returns:
        str: A general response to indicate the function is completed.
    """
    
    current_tags = get_all_tags()
    
    for tag_to_check in tags_to_check:
        # # # # Change this to a log entry:
        print(f"Checking: {tag_to_check}")
        
        if tag_to_check in current_tags:
            # # # # Change this to a log entry:
            print(f"{tag_to_check} is present")
            
        else:
            # # # # Change this to a log entry:
            #print(f"{tag_to_check} is not present")
            add_tag(tag_to_add = tag_to_check)
            #print(f"{tag_to_check} added")
                
    return "tag checking completed"


def get_all_articles():
    """_summary_
    Collects all of the articles from the articles table.
    
    Returns:
        queryset: all articles in the articles table
    """
    
    try:
        # --- Get all of the articles reference_id's:
        all_articles = Articles.objects.values_list("reference_id", flat = True)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return error_message
    
    else:
        return all_articles


def add_article_views_count(article_ref_id: int, article_views: int):
    """_summary_
    This function will add the number of views and the difference from the last
    record in the database for a given article.
    
    Args:
        article_ref_id (int): The article ref id to use.
        article_views (int): The number of views from the article.

    Returns:
        str: A message indicating the completion of the function.
    """
    
    # --- Get the name of the function that called this one@
    calling_function = stack()[1][3]
    
    # --- Get the article_od from the reference_id that was passed as an argument:
    article = Articles.objects.get(reference_id = article_ref_id)
    article_id = article.article_id
    
    # --- Set the values for the count and difference count:
    count = int(article_views)
    difference_count = int(0)
    
    # --- Check if the calling function is not named "add_article". If it isn't, 
    # --- perform the steps in the if statement:
    if calling_function != "add_article":
        # --- Get the last entry in the article_views table:
        last_article_views_count = ArticleViews.objects.filter(article_views_article_id_fk = article_id).latest("date_added")
        
        # --- Determine difference between last and new count
        difference_count = int(count - last_article_views_count.count)
    
    # --- Perform the creation of an entry into the article_views table:
    try:
        ArticleViews.objects.create(article_views_article_id_fk = Articles.objects.get(article_id = article_id),
                                    count = count,
                                    change = difference_count)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return f"Error: add_article_views_count: {error_message}"
    
    else:   
        return "completed"


def add_article_likes_count(article_ref_id:int, article_likes: int):
    """_summary_
    This function will add the number of likes and the difference from the last
    record in the database for a given article.
    
    Args:
        article_ref_id (int): The article ref id to use.
        article_likes (int): The number of likes from the article.

    Returns:
        str: A message indicating the completion of the function.
    """
    
    # --- Get the name of the function that called this one@
    calling_function = stack()[1][3]
    
    # --- Get the article_id from the reference_id that was passed as an argument:
    article = Articles.objects.get(reference_id = article_ref_id)
    article_id = article.article_id
    
    # --- Set the values for the count and difference count:
    count = int(article_likes)
    difference_count = int(0)
    
    # --- Check if the calling function is not named "add_article". If it isn't, 
    # --- perform the steps in the if statement:
    if calling_function != "add_article":
        # --- Get the last entry in the article_views table:
        last_article_likes_count = ArticleLikes.objects.filter(article_likes_article_id_fk = article_id).latest("date_added")
        
        # --- Determine difference between last and new count
        difference_count = int(count - last_article_likes_count.count)
    
    # --- Perform the creation of an entry into the article_views table:
    try:
        ArticleLikes.objects.create(article_likes_article_id_fk = Articles.objects.get(article_id = article_id),
                                    count = count,
                                    change = difference_count)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return f"Error: add_article_likes_count: {error_message}"
    
    else:   
        return "completed"


def add_article_comments_count(article_ref_id: int, article_comments: int):
    """_summary_
    This function will add the number of comments and the difference from the last
    record in the database for a given article.
    
    Args:
        article_ref_id (int): The article ref id to use.
        article_comments (int): The number of views from the article.

    Returns:
        str: A message indicating the completion of the function.
    """
    
    # --- Get the name of the function that called this one@
    calling_function = stack()[1][3]
    
    # --- Get the article_id from the reference_id that was passed as an argument:
    article = Articles.objects.get(reference_id = article_ref_id)
    article_id = article.article_id
    
    # --- Set the values for the count and difference count:
    count = int(article_comments)
    difference_count = int(0)
    
    # --- Check if the calling function is not named "add_article". If it isn't, 
    # --- perform the steps in the if statement:
    if calling_function != "add_article":
        # --- Get the last entry in the article_views table:
        last_article_comments_count = ArticleComments.objects.filter(article_comments_article_id_fk = article_id).latest("date_added")
        
        # --- Determine difference between last and new count
        difference_count = int(count - last_article_comments_count.count)
    
    # --- Perform the creation of an entry into the article_views table:
    try:
        ArticleComments.objects.create(article_comments_article_id_fk = Articles.objects.get(article_id = article_id),
                                       count = count,
                                       change = difference_count)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return f"Error: add_article_comments_count: {error_message}"
    
    else:   
        return "completed"
    

def add_article(article, user_id:int):
    """_summary_
    This function will take the name of a tag and add it to the Tags table in the database.
    
    Args:
        tag_to_add (str): The tag that needs to be added.

    Returns:
        String: Either an error is returned or an added tag message is returned.
    """

    article_details = article    
    
    try:
        # --- Create a new article in the articles table:
        article = Articles.objects.create(
            reference_id = article_details["id"],
            title = article_details["title"],
            is_published = article_details["published"],
            published_date = article_details["published_at"], 
            url = article_details["url"],
            article_user_id_fk_id = user_id,
        )
    
    except Exception as error_message:
        # # # # Change this to a log entry:
        return error_message
    
    else:
        # --- Add each tag in the article to the article_tags table:
        
        for tag in article_details["tag_list"]:
            
            try:
                # --- Get the tag from the Tags table and add it to the
                # --- article_tags table     
                tag_ref_id = Tags.objects.get(name = tag)
                article.tags.add(tag_ref_id.tag_id)

            except Exception as error_message:
                # # # # Change this to a log entry:
                return error_message
            
            else:
                # # # # Change this to a log entry:
                print(f"Added tag {tag} to article {article_details['id']}")


    add_article_views_count(article_ref_id = article.reference_id,
                            article_views = article_details["page_views_count"])
    
    add_article_likes_count(article_ref_id = article.reference_id,
                            article_likes = article_details["public_reactions_count"])
    
    add_article_comments_count(article_ref_id = article.reference_id,
                               article_comments = article_details["comments_count"])
                
    return f"Article \"{article.title}\" added successfully"