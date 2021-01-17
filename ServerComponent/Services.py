import prometheus_client as prom

from Analysers.Factories import SocialMediaAnalysersFactory, NewsAnalysersFactory
from Analysers.Handlers import NewsFilterSocialMediaHandler
from Analysers.Models import AnalysisResult
from DataLayer.DataSetEntry import TwitterDataSetEntryUnlabeled
from TextExtraction.APIs import TwitterAPI, TextAPI
from Analysers.SubjectRelevance import calculate_maximum_similarity_mean

prom.start_http_server(8000)

req_summary = prom.Summary('response_metrics', 'Time spent processing a request')
c = prom.Counter('my_exception_counter', 'Validate database values')


class AnalysisService:
    def __init__(self):
        self.socialMediaFactory = SocialMediaAnalysersFactory()
        self.newsFactory = NewsAnalysersFactory()

    @req_summary.time()
    @c.count_exceptions()
    def analyse_request(self, html, url):
        if url != "":
            result = self.analyse_twitter_post(html, url)
            return result
        else:
            return "facebook"
            # call text extraction from fb

    def analyse_twitter_post(self, html, url):

        handler = NewsFilterSocialMediaHandler()
        followers_number = TwitterAPI.getFollowers(TwitterAPI.getProfileName(url))
        if TwitterAPI.checkVerifiedAccount(TwitterAPI.getProfileName(url)):
            verified = 1
        else:
            verified = 0
        tweets_number = float(TwitterAPI.getTweets(html))
        retweets = TwitterAPI.getRetweets(html)
        quote_tweets = TwitterAPI.getQuoteTweets(html)
        likes_number = TwitterAPI.getLikes(html)
        words_number = TextAPI.getWordsNumber(TwitterAPI.getDataFromTwitter(html))
        wrong_words = TextAPI.getWrongWordsNumbers(TwitterAPI.getDataFromTwitter(html))
        correct_words = words_number - wrong_words
        if words_number != 0:
            grammar_index = (correct_words / words_number)
        else:
            grammar_index = 0
        subject_relevance = calculate_maximum_similarity_mean(TwitterAPI.getDataFromTwitter(html))
        post = TwitterDataSetEntryUnlabeled(followers_number, verified, tweets_number, retweets, quote_tweets,
                                            likes_number,
                                            grammar_index, subject_relevance)
        result = AnalysisResult()
        handler.handle(post, result)
        message = result.elements[0].validation_message
        return message

    def analyse_news_article(self, request):
        filter_handler = self.newsFactory.createNewsFilterHandler()
        common_sense_handler = self.newsFactory.createCommonSenseHandler()
        fact_check_handler = self.newsFactory.createCommonSenseHandler()
        inductive_handler = self.newsFactory.createInductiveHandler()
        filter_handler.set_next(common_sense_handler) \
            .set_next(fact_check_handler) \
            .set_next(inductive_handler)
        result = AnalysisResult()
        filter_handler.handle(request, result)
        return result
