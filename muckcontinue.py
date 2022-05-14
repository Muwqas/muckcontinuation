# this bot was made by u/hananelroe on reddit
import thefuzz.fuzz as fuzz
from thefuzz import *
import praw

print(praw.__version__)

Muck_list = ["muck", "muck.", "muck!", "muck?",
             "mück", "mück.", "mück!", "mück?",
             "m u c k", "m\*ck", "kcum", "muk",
             "muuck"]

# initialize with appropriate values
client_id = ""
client_secret = ""
username = "MuckMuckHAH"
password = ""
user_agent = "mukc is intentional"
comment_content = "mukc?! M u C k     k C u M"

while True:
    # creating an authorized reddit instance
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)

    subreddit = reddit.subreddit("DaniDev")
    print("online")

    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            print(comment.body)
            # check if the comment is above 74% muck: (allows 1 wrong letter in a 4 letters word)
            for item in Muck_list:
                if fuzz.ratio(comment.body.lower(), item) > 74:
                    comment.reply(comment_content)
                    break  # exit Muck_list loop
    except KeyboardInterrupt:  # Ctrl-C - stop
        print("Bye!")
    except Exception as error:  # Any exception
        print(f"Error: {error}")
        print("Trying to restart...")
