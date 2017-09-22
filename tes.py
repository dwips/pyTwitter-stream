import tweepy
import json

auth = tweepy.OAuthHandler('QQRLbKUnsy01BzT7vOOQ3gHg8',  'ipkWaYalXjpRnqiCsobj8nMVss5wrnDvVspW1QInflyyjf7Pe7')
auth.set_access_token('193535811-7NTh8qhHArKnOC0I9uE4XB66KBey1u2MsJp0c5vZ',  'EERRbSYvdUpWt77usLDgwAG9YI1YNankbRTahPRymQz6j')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

username = 'HillaryClinton'

user = api.get_user(username)

for status in tweepy.Cursor(api.user_timeline, id=username).items(10):
    print(json.dumps(status._json))
    with open('data.txt','a') as outfile:
        json.dump(status._json, outfile)
