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
            post_content.append({"title":submission.title , "content": submission.selftext, "id": submission.id})
    except:
        print("Error Fetching Reddit Posts")

    return post_content

# given a post id, checks a txt file to see if post used yet or not
def unique_post(post_id):
    #Reddit post ID storage file path: storage/previous_post_ids.txt
    storage_folder_name = "storage"
    storage_file_name = "previous_post_ids.txt"
    folder_absolute_path = os.path.abspath(storage_folder_name)
    post_id_storage_file_path = os.path.join(folder_absolute_path, storage_file_name)

    if os.path.exists(post_id_storage_file_path):
        try:
            ids = []
            with open(post_id_storage_file_path, 'r') as file:
                # Read each line in the file
                for line in file:
                    # Append the line to the list (removing newline characters)
                    ids.append(line.strip())
            file.close() 
            # checks if post_id is in id list if list has non-zero length
            if len(ids) != 0:
                for id in ids:
                    if str(id).lower() == str(post_id).lower(): # if id used before return false (since checking for unique)
                        return False
            return True # if id not found, return true
        
        except: # this could be the
            print("Issue parsing id storage file -- Unique ID Assumed")
            return True
    else:
        print(f"Creating Empty Storage File Called: {storage_folder_name}/{storage_file_name}")
        
        #double check path doesn't exist
        if not os.path.exists(post_id_storage_file_path):
            os.makedirs(folder_absolute_path) #create folder
            open(post_id_storage_file_path, 'a').close() #open file in that folder (essentially creating the file)

            return True
        
#given a post id, loads that id into the file storing previously used post ids
def update_id_storage_file(id):
    #file path info
    storage_folder_name = "storage"
    storage_file_name = "previous_post_ids.txt"
    folder_absolute_path = os.path.abspath(storage_folder_name)
    post_id_storage_file_path = os.path.join(folder_absolute_path, storage_file_name)

    try:
        with open(post_id_storage_file_path, 'a') as f:
            complete_addition = str(id) + "\n"
            f.write(complete_addition)
        
        print(f"Appended Post ID {id} to Storage")
    except:
        print(f"ERROR Appending Post ID {id} to Storage")

