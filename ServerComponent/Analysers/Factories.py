from __future__ import annotations
from abc import ABC, abstractmethod

from Analysers.Handlers import  NewsFilterSocialMediaHandler, FactCheckSocialMediaHandler, CommonSenseSocialMediaHandler, \
    InductiveSocialMediaHandler, NewsFilterArticleHandler, FactCheckArticleHandler, CommonSenseArticleHandler, \
    InductiveArticleHandler


class AbstractFactory(ABC):
    @abstractmethod
    def createNewsFilterHandler(self):
        pass

    @abstractmethod
    def createFactCheckHandler(self):
        pass

    @abstractmethod
    def createCommonSenseHandler(self):
        pass

    @abstractmethod
    def createInductiveHandler(self):
        pass


class SocialMediaAnalysersFactory(AbstractFactory):
    def createNewsFilterHandler(self) -> NewsFilterSocialMediaHandler:
        pass

    def createFactCheckHandler(self) -> FactCheckSocialMediaHandler:
        pass

    def createCommonSenseHandler(self) -> CommonSenseSocialMediaHandler:
        pass

    def createInductiveHandler(self) -> InductiveSocialMediaHandler:
        pass


class NewsAnalysersFactory(AbstractFactory):
    def createNewsFilterHandler(self) -> NewsFilterArticleHandler:
        pass

    def createFactCheckHandler(self) -> FactCheckArticleHandler:
        pass

    def createCommonSenseHandler(self) -> CommonSenseArticleHandler:
        pass

    def createInductiveHandler(self) -> InductiveArticleHandler:
        pass
