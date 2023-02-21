# --- Import required modules and libraries:
from ..models import Articles, ArticleLikes, ArticleComments, Tags


def get_all_tags():
    """_summary_
    Collects all of the tags from the tags table.
    
    Returns:
        list: all tags in the tags table.
    """
    
    try:
        all_tags = Tags.objects.values_list('name', flat = True)
        
    except:
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
        Tags.objects.create(name = tag_to_add)
        
    except:
        return "Error"
    
    else:    
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
        print(f"Checking: {tag_to_check['name']}")
        
        if tag_to_check["name"] in current_tags:
            print(f"{tag_to_check['name']} is present")
            #print(f"{current_tags['id']}")
            
        else:
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
        all_articles = Articles.objects.all()
        
    except:
        error_msg = "error"
        return error_msg
    
    else:
        return all_articles


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
        article = Articles.objects.create(
            reference_id = article_details["id"],
            title = article_details["title"],
            is_published = article_details["published".capitalize],
            published_date = article_details["published_at"], 
            url = article_details["url"]
        )
    
    except Exception as error_message:
        print(f"Error: {error_message}")
    
    else:
        for tag in article_details["tag_list"]:
            
            try:
                tag_ref_id = Tags.objects.get(name = tag)      
                article.tags.add(tag_ref_id.tag_id)

            except Exception as error_message:
                print(f"Error: {error_message}")
            
            else:   
                print(f"Added tag {tag}")
                
    return "Article added successfully"

