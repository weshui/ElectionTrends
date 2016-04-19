import filter
import tweet
import TweetReader

# filenmae

filePath = "/Users/anirudhnair/Dropbox/WORK/lecNotes/cs410/project/test.json"
configXml = "/Users/anirudhnair/Documents/workspace/TwitterAnalysis/filter.xml"
outFile = "/Users/anirudhnair/Dropbox/WORK/lecNotes/cs410/project/test_out.json"
reader = TweetReader.TweetReader(filePath)
filter_ = filter.Filter(configXml)
oFP = open(outFile,'w')

while (True):
    tweet_ = reader.next()
    if (tweet_ == None):
        break
    
    if( filter_.FilterTweet(tweet_) ):
        oFP.write(tweet_.GetJSONStr() + "\n")
        
        
        
oFP.close()