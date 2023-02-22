# --- Import required modules and libraries:
from ..models import Articles, ArticleLikes, ArticleComments, Tags


def get_all_tags():
    """_summary_
    Collects all of the tags from the tags table.
    
    Returns:
        list: all tags in the tags table.
    """
    
    try:
        # --- Get all of the tag names:
        all_tags = Tags.objects.values_list('name', flat = True)
        
    except:
        # # # # Change this to a log entry:
        error_msg = "error"
        return error_msg
    
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
        
    except:
        # # # # Change this to a log entry:
        return "Error"
    
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
        print(f"Checking: {tag_to_check['name']}")
        
        if tag_to_check["name"] in current_tags:
            # # # # Change this to a log entry:
            print(f"{tag_to_check['name']} is present")
            
        else:
            # # # # Change this to a log entry:
            print(f"{tag_to_check['name']} is not present")
            add_tag(tag_to_add = tag_to_check["name"])
            print(f"{tag_to_check['name']} added")
                
    return "tag checking completed"


def get_all_articles():
    """_summary_
    Collects all of the articles from the articles table.
    
    Returns:
        queryset: all articles in the articles table
    """
    
    try:
        # --- Get all of the articles reference_id's:
        all_articles = Articles.objects.values_list("reference_id" ,flat = True)
        
    except Exception as error_message:
        # # # # Change this to a log entry:
        return error_message
    
    else:
        return all_articles


def add_article_views_count():
    pass


def add_article_likes_count():
    pass


def add_article_comments_count():
    pass
    

def add_article():
    """_summary_
    This function will take the name of a tag and add it to the Tags table in the database.
    
    Args:
        tag_to_add (str): The tag that needs to be added.

    Returns:
        String: Either an error is returned or an added tag message is returned.
    """

    article_details = {
        "type_of": "article",
        "id": 1203386,
        "title": "What I Learned From Doing The 100 Days of Code Challenge",
        "description": "Introduction  Lessons Learned   Create A Schedule You Don't Need To Spend A Fortune To Learn Learn...",
        "published_at": "2022-09-26T12:21:52.632Z",
        "slug": "what-i-learned-from-doing-the-100-days-of-code-challenge-4md4",
        "path": "/dev_neil_a/what-i-learned-from-doing-the-100-days-of-code-challenge-4md4",
        "url": "https://dev.to/dev_neil_a/what-i-learned-from-doing-the-100-days-of-code-challenge-4md4",
        "published": True,
        "comments_count": 0,
        "public_reactions_count": 0,
        "page_views_count": 42,
        "published_timestamp": "2022-09-26T12:21:52Z",
        "body_markdown": "Removed as it's the body of the article",
        "positive_reactions_count": 0,
        "cover_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--VgUXsbyq--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/67g2ekfytyhxsrliuynj.jpeg",
        "tag_list": [
            "100daysofcode",
            "python",
            "javascript",
            "codenewbie"
        ],
        "canonical_url": "https://dev.to/dev_neil_a/what-i-learned-from-doing-the-100-days-of-code-challenge-4md4",
        "reading_time_minutes": 7,
        "user": {
            "name": "dev_neil_a",
            "username": "dev_neil_a",
            "twitter_username": "dev_neil_a",
            "github_username": "York13Pud",
            "user_id": 857210,
            "website_url": "https://www.linkedin.com/in/neil-allwood/",
            "profile_image": "https://res.cloudinary.com/practicaldev/image/fetch/s---Y4hmlhp--/c_fill,f_auto,fl_progressive,h_640,q_auto,w_640/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/857210/26770d9b-d135-46f0-9439-0ec70428ec63.png",
            "profile_image_90": "https://res.cloudinary.com/practicaldev/image/fetch/s--SZy6y74T--/c_fill,f_auto,fl_progressive,h_90,q_auto,w_90/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/857210/26770d9b-d135-46f0-9439-0ec70428ec63.png"
        }
    }
    
    
    try:
        # --- Create a new article in the articles table:
        article = Articles.objects.create(
            reference_id = article_details["id"],
            title = article_details["title"],
            is_published = article_details["published"],
            published_date = article_details["published_at"], 
            url = article_details["url"],
            article_user_id_fk_id = 2,
        )
    
    except Exception as error_message:
        # # # # Change this to a log entry:
        print(f"Error: {error_message}")
    
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
                print(f"Error: {error_message}")
            
            else:
                # # # # Change this to a log entry:
                print(f"Added tag {tag} to article {article_details['id']}")
    
    add_article_views_count(article_id = article["id"],
                            article_likes = article_details["page_views_count"])
    
    add_article_likes_count(article_id = article["id"],
                            article_likes = article_details["public_reactions_count"])
    
    add_article_comments_count(article_id = article["id"],
                               article_likes = article_details["comments_count"])
                
    return "Article added successfully"
