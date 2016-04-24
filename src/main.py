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
totalTweets = 0
totalFilteredTweets = 0
while (True):
    tweet_ = reader.next()
    if (tweet_ == None):
        break
    totalTweets = totalTweets + 1
    if( filter_.FilterTweet(tweet_) ):
        oFP.write(tweet_.GetJSONStr())
        totalFilteredTweets = totalFilteredTweets + 1
        
        
        
oFP.close()
print "Total tweets processed " + str(totalTweets) + " \n"
print "Total tweets that passed the filter " + str(totalFilteredTweets) + " \n"