# --- Import required modules and libraries:


# --- Make API call to collect published articles:


# --- Check for a HTTP 200 response. If not 200, log and end process:


# --- Call function to query articles table to collect all articles:


# --- Query article ref ID against each article in API JSON / Pandas return:


# --- call function to query tags table to collect all tag names:


# --- Call function to check article tags:


# --- Once tag check is completed, call function to query tags table to collect all tag names
# --- and add article to articles table.
# --- Then add the tags / article to the article_tags table where needed:


# --- Problem on diagram: The orange functions don't run after an article is added.