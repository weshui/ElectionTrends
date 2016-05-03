# class that represent a Tweet
# has methods for accessing differnt elements of the TweetReader
import json
from datetime import datetime
from dateutil import parser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


class Tweet:
    
    def __init__(self,tweet_json):
        self.json_str = tweet_json
        tweet = json.loads(tweet_json)
        self.id = tweet['id_str']
        # read tweet
        self.text = tweet['text']
        #read hashtags
        if tweet['entities']['hashtags']:
            self.hashtags = []
            hashtag_objs =  tweet['entities']['hashtags'] 
            for hashtag in hashtag_objs:
                self.hashtags.append(hashtag['text'])
        else:
            self.hashtags = None
        #read mentions
        if tweet['entities']['user_mentions']:
            self.user_mentions =  []
            user_mention_obj = tweet['entities']['user_mentions'] 
            for user_mention in user_mention_obj:
                self.user_mentions.append(user_mention['screen_name'])
        else:
            self.user_mentions = None
        #read date
        self.date = parser.parse(tweet['created_at'])
        
        #read location
        if tweet['place']:
            self.location = tweet['place']['full_name']
        else:
            self.location = None
        
        
    def GetJSONStr(self):
        return self.json_str
    
    def GetTweet(self):
        return self.text
    
    def GetHashTags(self):
        return self.hashtags
        
    def GetUserMentions(self):
        return self.user_mentions
        
    def GetDate(self):
        return self.date
        
    def GetLocation(self):
        return self.location

    def GetSentiment(self):
        sentiments = sid.polarity_scores("The food is delicious")
        return (sentiments["pos"], sentiments["neg"])


    def createObj(self):
        obj = {}
        obj["location"] = self.GetLocation()
        obj["text"] = self.GetTweet()
        obj["user_mentions"] = self.GetUserMentions()
        obj["hashtags"] = self.GetHashTags()
        obj["sentiment"] = self.GetSentiment()
        obj["date"] = self.GetDate()
        return obj

    def dumpSentimentJSON(self, fname):
        with open(fname, "a") as outFile:
            myfile.write(json.dumps(outFile))
