# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.
import requests
from pprint import pprint
import json
import os
import praw


user_name = os.environ['reddit_username']
reddit_password = os.environ['reddit_password']

user_pass_dict = {
     "user":user_name,
     "passwd":reddit_password,
     "api_type":"json"
 }

client = requests.session()

r = client.post("https://www.reddit.com/api/login", data=user_pass_dict)

j = json.loads(r.content)

pprint(j)