from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import StringIO
import os
import json
import csv

# == OAuth Authentication ==
consumer_key="XXXXXXXXXXXXXXXXXX"
consumer_secret="XXXXXXXXXXXXXXXXXX"

access_token="XXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXX"

class StdOutListener(StreamListener):

	def on_data(self, data):
	    if not data == None:
	        parsed_data = json.loads(data)
	        tweet_string = None
            try:
                if parsed_data and 'text' in parsed_data.keys() and parsed_data['created_at'] and parsed_data['coordinates']:
                    tweet_string = parsed_data['created_at'].encode('utf-8')
                    d = datetime.strptime(parsed_data['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                    t = d.strftime('%Y/%m/%d %H:%M:%S')
                    tweet = parsed_data['text'].encode('utf-8')
                    tweet_string = parsed_data['coordinates']['coordinates'][0],parsed_data['coordinates']['coordinates'][1],t,tweet
                    if " bitch " in tweet:
                        with open('bad2.csv', 'a') as acsv:
                            w = csv.writer(acsv)
                            w.writerow(tweet_string)
                            print tweet_string
                    if " ass " in tweet:
                        with open('bad3.csv', 'a') as acsv:
                            w = csv.writer(acsv)
                            w.writerow(tweet_string)
                            print tweet_string
                    if " shit " in tweet:
                        with open('bad3.csv', 'a') as acsv:
                            w = csv.writer(acsv)
                            w.writerow(tweet_string)
                            print tweet_string
                    if " fuck " in tweet:
                        with open('bad3.csv', 'a') as acsv:
                            w = csv.writer(acsv)
                            w.writerow(tweet_string)
                            print tweet_string

            except TypeError, e:
                print "Type Error",e

            except KeyError, e:
                print "Key Error", e

	def on_error(self, status):
		print status

with open('bad3.csv', 'wt') as acsv:
    w = csv.writer(acsv)
    w.writerow(['Long', 'Lat', 'Time', 'Tweet'])

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth,l)
    stream.filter(locations=[-125,25,-65,48],async=False )
