# --- Import required modules and libraries:
from ..models import Articles, ArticleLikes, ArticleComments, Tags

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
    data = tag_to_add
    tag_to_create = Tags.objects.create(name = data)
    return f"Added tag {data}"


def check_tag(tags_to_check: list, current_tags: list):
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
        
    for tag_to_check in tags_to_check:
        # print("Stage 1")
        print(f"Checking: {tag_to_check['name']}")
        
        if tag_to_check["name"] in current_tags:
            # print("Stage 2")
            print(f"{tag_to_check['name']} is present")
        else:
            # print("Stage 3")
            print(f"{tag_to_check['name']} is not present")
            # print("Stage 4")
            add_tag(tag_to_add = tag_to_check["name"])
            print(f"{tag_to_check['name']} added")
                
    return "tag checking done"


# http://127.0.0.1:8000/stats/testing/