from __future__ import annotations
from abc import ABC, abstractmethod

from Handlers import NewsFilterHandler, FactCheckHandler, CommonSenseHandler, InductiveHandler


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
    def createNewsFilterHandler(self) -> NewsFilterHandler:
        pass

    def createFactCheckHandler(self) -> FactCheckHandler:
        pass

    def createCommonSenseHandler(self) -> CommonSenseHandler:
        pass

    def createInductiveHandler(self) -> InductiveHandler:
        pass


class NewsAnalysersFactory(AbstractFactory):
    def createNewsFilterHandler(self):
        pass

    def createFactCheckHandler(self):
        pass

    def createCommonSenseHandler(self):
        pass

    def createInductiveHandler(self):
        pass
