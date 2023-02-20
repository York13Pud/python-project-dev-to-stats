# --- Import required modules and libraries:
from ..models import Articles, ArticleLikes, ArticleComments, Tags

def get_all_articles():
    """_summary_
    Collects all of the articles from the articles table.
    
    Returns:
        _type_: _description_
    """
    
    print("start")
    
    all_articles = Articles.objects.all()
    
    print(type(all_articles))
    
    return all_articles
    