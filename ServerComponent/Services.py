from Analysers.Factories import SocialMediaAnalysersFactory, NewsAnalysersFactory
from Analysers.Models import AnalysisResult


class AnalysisService:
    def __init__(self):
        self.socialMediaFactory = SocialMediaAnalysersFactory()
        self.newsFactory = NewsAnalysersFactory()

    def analyseRequest(self, request):
        if request == "social media":
            return self.analyseSocialMediaPost(request)
        else:
            return self.analyseNewsArticle(request)

    def analyseSocialMediaPost(self, request):
        filterHandler = self.socialMediaFactory.createNewsFilterHandler()
        commonSenseHandler = self.socialMediaFactory.createCommonSenseHandler()
        factCheckHandler = self.socialMediaFactory.createCommonSenseHandler()
        inductiveHandler = self.socialMediaFactory.createInductiveHandler()
        filterHandler.set_next(commonSenseHandler) \
            .set_next(factCheckHandler) \
            .set_next(inductiveHandler)
        result = AnalysisResult()
        filterHandler.handle(request, result)
        return result

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
