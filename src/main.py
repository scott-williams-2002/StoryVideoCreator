from reddit.Reddit_Handler import grab_posts 


#posts = grab_posts("offmychest", 3)
def chooseSubreddit(subreddit_list):
    print(f"Enter a number (0 - {len(subreddit_list)-1}) to select a subreddit")
    try:
        for i in range(len(subreddit_list)):
            print(f"{i} -> {subreddit_list[i]}")

        user_input = int(input(f"Choice (0 - {len(subreddit_list)-1}): "))
        print(f"You chose the subreddit: {subreddit_list[user_input]}")
        return subreddit_list[user_input]
    except:
        print("Enter your own subreddit name")
        subreddit_name = str(input("Name: "))
        return subreddit_name


def main():
    subreddit_list = ["offmychest","AskMen"]
    subreddit_name = chooseSubreddit(subreddit_list=subreddit_list)





if __name__ == "__main__":
    main()