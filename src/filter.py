

import tweet
import TweetReader
from xml.etree import ElementTree



class Filter:
    
    def __init__(self,xmlPath):
        self.hashtags = []
        self.users = []
        self.words = []
        self.issues = []
        with open(xmlPath, 'rt') as f:
            tree = ElementTree.parse(f)
        root = tree.getroot()
        for node in root:
            tag = node.tag
            data = node.attrib['data']
            if(tag == "HashTags"):
                self.hashtags = data.split(',')
            elif (tag =="User"):
                self.users = data.split(',')
            elif (tag =="Words"):
                self.words = data.split(',')
            elif (tag =="IssueTags"):
                self.issues = data.split(',')
                
                    
                
    
    def FilterTweet(self,tweet):
        if(self.HashTagFilter(tweet) or self.UserMentionFilter(tweet) or 
           self.WordFilter(tweet) or self.IssueTagFilter(tweet)):
            return True
        else:
            return False
    
    def HashTagFilter(self,tweet):
        hashTags = tweet.GetHashTags()
        return self.SearchInArray(self.hashtags,hashTags)
    
    def UserMentionFilter(self,tweet):
        users_ = tweet.GetUserMentions()
        return self.SearchInArray(self.users,users_)
    
    def WordFilter(self,tweet):
        text = tweet.GetTweet()
        for word in self.words:
            if ( word in text ):
                return True
        return False
    
    def IssueTagFilter(self,tweet):
        hashTags = tweet.GetHashTags()
        return self.SearchInArray(self.issues,hashTags)

    def SearchInArray(self,searchFor,searchIn):
        for searchTerm in searchFor:
            if( searchTerm in searchIn):
                return True
        return False
        
