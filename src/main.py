from reddit.Reddit_Handler import grab_posts 


posts = grab_posts("offmychest", 3)

for each in posts:
    print(each["title"])
    print("")
    print(each["content"])