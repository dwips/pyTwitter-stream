__author__ = 'Abenk'

import tweepy
import re

auth = tweepy.OAuthHandler('QQRLbKUnsy01BzT7vOOQ3gHg8',  'ipkWaYalXjpRnqiCsobj8nMVss5wrnDvVspW1QInflyyjf7Pe7')
auth.set_access_token('193535811-7NTh8qhHArKnOC0I9uE4XB66KBey1u2MsJp0c5vZ',  'EERRbSYvdUpWt77usLDgwAG9YI1YNankbRTahPRymQz6j')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []
tweetsTgl = []
tweetsGeo = []
username = 'HillaryClinton'

user = api.get_user(username)

# print user.id_str
# print user.description
# print user.created_at
# print user.name

# c = tweepy.Cursor(api.search, q = 'banjir')

for status in tweepy.Cursor(api.user_timeline, id=username).items(1000):
    # print status.id_str

    # status.text.encode('ASCII','ignore')
    tweet = status.text.encode("ASCII",'ignore')
    tweetTgl= str(status.created_at)
    print [tweet, tweetTgl]
    # tweetGeo = str(status.coordinates['coordinates']) if status.coordinates is not None else 'unknown'
    # twitGeo = str(status.geo)
    # if re.search(r'(haha*)+',tweet):
    tweets.append(tweet)
    tweetsTgl.append(tweetTgl)
    # tweetsGeo.append(tweetGeo)
    # if re.search(r'^@[^ ]+', tweet):
    #     tweets.append(tweet)
    #     tweetsTgl.append(tweetTgl)
    #     print 'ini tweet reply'
    # elif re.search(r'^(RT |")@[^ ]+:', tweet):
    #     tweets.append(tweet)
    #     tweetsTgl.append(tweetTgl)
    #     print 'ini retweet'
        # hahahahhhahhhahhaha
        # (hah*)+

        # Tweet reply @jokowi: ...
        # RT @jokowi: ... / "@jokowi: ..."



import pandas

data_to_save = pandas.DataFrame({'TWEET': tweets, 'Tanggal': tweetsTgl})
excel_writer = pandas.ExcelWriter('contoh1.xlsx', engine='xlsxwriter',options={'encoding': 'utf-8'})
data_to_save.to_excel(excel_writer, sheet_name='Sheet1')
excel_writer.close()

