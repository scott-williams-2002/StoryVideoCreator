import praw
from dotenv import load_dotenv
import os

# grabs hottest n posts from subreddit
def grab_posts(subreddit_name, n_posts):
    load_dotenv()
    #reddit client
    reddit = praw.Reddit(
        client_id= os.getenv("CLIENT_ID"),
        client_secret= os.getenv("CLIENT_SECRET"),
        user_agent= os.getenv("USER_AGENT"),
    )
    #try to populate post contents into list
    post_content = []
    try:
        # adds post title and content to list of dictionaries
        for submission in reddit.subreddit(subreddit_name).top(limit=n_posts):
            post_content.append({"title":submission.title , "content": submission.selftext})
    except:
        print("Error Fetching Reddit Posts")

    return post_content