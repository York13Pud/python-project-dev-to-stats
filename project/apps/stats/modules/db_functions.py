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
        queryset: all tags in the tags table
    """
    
    try:
        all_tags = Tags.objects.all()
        
    except:
        error_msg = "error"
        return error_msg
    
    else:
        return all_tags