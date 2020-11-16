from __future__ import annotations
from abc import ABC, abstractmethod

class ParseDataComponent(ABC):
    @abstractmethod
    def extractData(self):
        pass

    @abstractmethod
    def structureData(self):
        pass

    @abstractmethod
    def checkDatainWhiteList(self):
        pass

    @abstractmethod
    def handleResult(self):
        pass

class ParseDataComposite(ParseDataComponent):
    def extractData(self):
        #TODO get the components(title, body, author, ..)
        pass

    def structureData(self):
        #TODO establish wich component it is
        pass

    def checkDatainWhiteList(self):
        #TODO check if the article it is or not in the preset WhiteList
        pass

    def handleResult(self):
        #TODO
        pass
