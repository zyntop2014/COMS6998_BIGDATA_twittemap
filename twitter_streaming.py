# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch, RequestsHttpConnection
import time



# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '838110956660080641-HTzfzOvyVLfMNiMwMaAkn9xMBtQUEVk'
ACCESS_SECRET = 'euVN5HZsIBJttx5JgrxbiBcVKdm4KqdC12FSmEX2GOKSt'
CONSUMER_KEY = 'KMUioXv68EVY2hi4wsjbQhJ7n'
CONSUMER_SECRET = 'euVksyfB0hmm0Xc92GPoq8bH8ZHhYD4SPhh0FpettqCSpGHefi'



oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'


es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print(es.info())



# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# collect the Twitter API to collect data for days or even longer. 
tweet_count = 1
for tweet in iterator:  
    try:    
        if 'text' in tweet: # only messages contains 'text' field is a tweet  
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
          
            es.index(index="tweet", doc_type="tweetmap", id= tweet['id'], body= tweet)
            tweet_count += 1

    except:
        continue

    
    #if tweet_count > 30000:
     #  break 

