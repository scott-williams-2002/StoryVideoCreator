from reddit.Reddit_Handler import grab_posts, unique_post, update_id_storage_file
from user_input.ui_functions import chooseSubreddit


def main():
    subreddit_list = ["offmychest","AskMen", "AITAH"]
    subreddit_name = chooseSubreddit(subreddit_list=subreddit_list)

    #print(grab_posts(subreddit_name, 1))
    print(unique_post(1))
    update_id_storage_file(43)
    print(unique_post(43))





if __name__ == "__main__":
    main()