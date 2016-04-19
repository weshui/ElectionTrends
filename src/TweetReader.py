
# init with file
#call next to read each Line
# return a tweet Instance
# nill for EOF

import tweet
class TweetReader:
    "reader for file with json data"
    
    
    def __init__(self, filepath):
        self.m_sFilePath = filepath
        self.fp = open(self.m_sFilePath)
        
    def next(self):
        line = self.fp.readline()
        if not line:
            return None
        else:
            return tweet.Tweet(line)
        
    def close(self):
        self.fp.close()