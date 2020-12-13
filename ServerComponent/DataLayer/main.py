import random

from Analysers.Handlers import NewsFilterSocialMediaHandler
from Analysers.Models import AnalysisResult
from DataLayer.DataSetEntry import TwitterDataSetEntryUnlabeled

handler = NewsFilterSocialMediaHandler()
likes = random.randint(0, 500000)
verified = random.randint(0, 1)
tweets_number = random.randint(0, 30000)
retweets = random.randint(0, 25000)
quote_tweets = random.randint(0, 4000)
likes_number = random.randint(0, 100000)
grammar_index = random.randint(0, 100) / 100
subject_relevance = random.randint(0, 100)
post = TwitterDataSetEntryUnlabeled(likes, verified, tweets_number, retweets, quote_tweets, likes_number, grammar_index,
                                    subject_relevance)
result = AnalysisResult()
handler.handle(post, result)
print("Likes : {}".format(likes))
print("Verified : {}".format(verified))
print("Tweets Number : {}".format(tweets_number))
print("Retweets : {}".format(retweets))
print("Quote Tweets : {}".format(quote_tweets))
print("Likes Number : {}".format(likes_number))
print("Grammar Index : {}".format(grammar_index))
print("Subject Relevance : {}".format(subject_relevance))

for element in result.elements:
    print(element.validation_result)
    print(element.validation_message)
