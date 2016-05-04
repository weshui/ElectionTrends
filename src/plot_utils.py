from xml.etree import ElementTree
from collections import defaultdict
from os.path import exists
import json
from dateutil import parser


def read_xml(xml_file_path):
    users = defaultdict(lambda: defaultdict())
    with open(xml_file_path, 'rt') as f:
        tree = ElementTree.parse(f)
    root = tree.getroot()
    for child in root:
        tag = child.tag
        if tag == "Mapping":
            for node in child:
                name = node.get('name')
                print name
                text_mentions = node.get('words')
                hashtag_mentions = node.get('hashTag').split(',')
                user_mentions = node.get('user')

                users[name]['text'] = text_mentions
                users[name]['hashtags'] = hashtag_mentions
                users[name]['user'] = user_mentions

    return users


def popularity_vs_time():
    candidates = read_xml('./filter.xml')
    popularity = defaultdict(lambda: defaultdict(int))
    for month in ['Feb', 'Mar']:
        for day in range(1, 31):
            fname = './../../tweets/{}/analyzed/{}.json'.format(
                month, "%02d" % day)
            if not exists(fname):
                continue
            popularity_one_day = get_popularity_one_file(fname, candidates)
            for candidate in popularity_one_day:
                for date_time in popularity_one_day[candidate]:
                    popularity[candidate][
                        date_time] += popularity_one_day[candidate][date_time]

    for candidate in popularity:

        with open(candidate + '_popularity.csv', 'w') as cand_file:
            dates = popularity[candidate].keys()
            dates.sort()
            for date in dates:
                cand_file.write(
                    str(date[0]) + '\t' + str(date[1]) + '\t' + str(popularity[candidate][date]) + '\n')
    return popularity


def get_popularity_one_file(fname, candidates):
    popularity = defaultdict(lambda: defaultdict(int))
    with open(fname, 'r') as jsonFile:
        numTweets = 0
        for line in jsonFile:
            curr_tweet = json.loads(line)
            tweet_datetime = parser.parse(curr_tweet['date'])
            tweet_date = (tweet_datetime.month, tweet_datetime.day)
            for cand in candidates:
                candidate = candidates[cand]
                if candidate['text'] in curr_tweet['text']:
                    popularity[cand][tweet_date] += 1
                    continue
                if curr_tweet['hashtags'] and any([hashtag in curr_tweet['hashtags'] for hashtag in candidate['hashtags']]):
                    popularity[cand][tweet_date] += 1
                    continue
                if curr_tweet['user_mentions'] and candidate['user'] in curr_tweet['user_mentions']:
                    popularity[cand][tweet_date] += 1
                    continue
            numTweets += 1
        print "Analyzed", numTweets, "tweets ..."
    return popularity

print popularity_vs_time()
