import boto3
import random
import time
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('api_auth.cfg')

#This is the super secret information
access_token = parser.get('api_tracker', 'access_token')
access_token_secret = parser.get('api_tracker', 'access_token_secret')
consumer_key = parser.get('api_tracker', 'consumer_key')
consumer_secret = parser.get('api_tracker', 'consumer_secret')
aws_key_id =  parser.get('api_tracker', 'aws_key_id')
aws_key =  parser.get('api_tracker', 'aws_key')

DeliveryStreamName = 'twitter-stream'

client = boto3.client('firehose', region_name='eu-west-1',
                          aws_access_key_id=aws_key_id,
                          aws_secret_access_key=aws_key
                          )

#This is a basic listener that just prints received tweets and put them into the stream.
class StdOutListener(StreamListener):

    def on_data(self, data):

        client.put_record(DeliveryStreamName=DeliveryStreamName,Record={'Data': json.loads(data)["text"]})

        print json.loads(data)["text"]

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['realmadrid'])
