import prometheus_client as prom

from Analysers.Factories import SocialMediaAnalysersFactory, NewsAnalysersFactory
from Analysers.Handlers import NewsFilterSocialMediaHandler
from Analysers.Models import AnalysisResult
from DataLayer import ValidateDatabase
from DataLayer.DataSetEntry import TwitterDataSetEntryUnlabeled
from TextExtraction.APIs import TwitterAPI, TextAPI

prom.start_http_server(8000)

req_summary = prom.Summary('response_metrics', 'Time spent processing a request')
c = prom.Counter('my_database_validation', 'Validate database values')


class AnalysisService:
    def __init__(self):
        self.socialMediaFactory = SocialMediaAnalysersFactory()
        self.newsFactory = NewsAnalysersFactory()

    @req_summary.time()
    #@c.count_exceptions()
    def analyseRequest(self, html, url):
        if url != "":
            result = self.analyseTwitterPost(html, url)
            return result
        else:
            return "facebook"
            # call text extraction from fb

    def analyseTwitterPost(self, html, url):

        handler = NewsFilterSocialMediaHandler()
        followers_number = float(TwitterAPI.getFollowers(TwitterAPI.getProfileName(url)).replace(",", ""))
        if TwitterAPI.checkVerifiedAccount(TwitterAPI.getProfileName(url)) :
            verified = 1
        else: verified = 0
        tweets_number = float(TwitterAPI.getTweets(TwitterAPI.getProfileName(url)).replace(",", ""))
        retweets = TwitterAPI.getRetweets(html)
        quote_tweets = TwitterAPI.getQuoteTweets(html)
        likes_number = TwitterAPI.getLikes(html)
        words_number = TextAPI.getWordsNumber(TwitterAPI.getDataFromTwitter(url))
        wrong_words = TextAPI.getWrongWordsNumbers(TwitterAPI.getDataFromTwitter(url))
        correct_words = words_number - wrong_words
        grammar_index = (correct_words / words_number)
        subject_relevance = 90
        post = TwitterDataSetEntryUnlabeled(followers_number, verified, tweets_number, retweets, quote_tweets,
                                            likes_number,
                                            grammar_index, subject_relevance)
        result = AnalysisResult()
        handler.handle(post, result)
        message = result.elements[0].validation_message
        return message

    def analyseNewsArticle(self, request):
        filterHandler = self.newsFactory.createNewsFilterHandler()
        commonSenseHandler = self.newsFactory.createCommonSenseHandler()
        factCheckHandler = self.newsFactory.createCommonSenseHandler()
        inductiveHandler = self.newsFactory.createInductiveHandler()
        filterHandler.set_next(commonSenseHandler) \
            .set_next(factCheckHandler) \
            .set_next(inductiveHandler)
        result = AnalysisResult()
        filterHandler.handle(request, result)
        return result

#    with c.count_exceptions():
 #       print("Start database validation.")
  #      ValidateDatabase.validate()
   #     print("End database validation.")
