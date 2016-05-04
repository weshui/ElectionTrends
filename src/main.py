import filter
import tweet
import TweetReader
from os.path import exists


def calculate_and_dump_sentiment():
    for month in ['Feb', 'Mar', 'Apr']:
        for day in range(1, 31):
            fname = './../../tweets/{}/{}.json'.format(month, "%02d" % day)
            if not exists(fname):
                continue
            print "Starting", month, day, "..."
            reader = TweetReader.TweetReader(fname)
            save_fname = '/'.join(fname.split('/')[:5] + ['analyzed'] + fname.split('/')[5:])
            #save_fname = fname[:-5] + '_filtered_analyzed' + fname[-5:]
            numTweets = 0
            while True:
                curr_tweet = reader.next()
                if curr_tweet is None:
                    break
                curr_tweet.dumpSentimentJSON(save_fname)
                numTweets += 1
            print "Analyzed", numTweets, "tweets ..."


def filter_tweets():
    filePath = "/Users/anirudhnair/Dropbox/WORK/lecNotes/cs410/project/test.json"
    configXml = "/Users/anirudhnair/Documents/workspace/TwitterAnalysis/filter.xml"
    outFile = "/Users/anirudhnair/Dropbox/WORK/lecNotes/cs410/project/test_out.json"
    reader = TweetReader.TweetReader(filePath)
    filter_ = filter.Filter(configXml)
    oFP = open(outFile, 'w')
    totalTweets = 0
    totalFilteredTweets = 0
    while (True):
        tweet_ = reader.next()
        if (tweet_ is None):
            break
        totalTweets = totalTweets + 1
        if(filter_.FilterTweet(tweet_)):
            oFP.write(tweet_.GetJSONStr())
            totalFilteredTweets = totalFilteredTweets + 1

    oFP.close()
    print "Total tweets processed " + str(totalTweets) + " \n"
    print "Total tweets that passed the filter " + str(totalFilteredTweets) + " \n"

if __name__ == "__main__":
	# filter_tweets()
    calculate_and_dump_sentiment()
