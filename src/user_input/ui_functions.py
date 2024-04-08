# This file stores all user input functions that could go in main to avoid clutter 

#called first in main to grab a subreddit from 
def chooseSubreddit(subreddit_list):
    print(f"Enter a number (0 - {len(subreddit_list)-1}) to select a subreddit")
    # asks user for number to choose list value -> subreddit name
    try: #try catch for mitigating out of bound error
        for i in range(len(subreddit_list)):
            print(f"{i} -> {subreddit_list[i]}")

        user_input = int(input(f"Choice (0 - {len(subreddit_list)-1}): "))
        print(f"You chose the subreddit: {subreddit_list[user_input]}")
        return subreddit_list[user_input]
    except: # enter a new subreddit name also possible
        print("Enter your own subreddit name")
        subreddit_name = str(input("Name: "))
        return subreddit_name