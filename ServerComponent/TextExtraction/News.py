from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class News:
    def __init__(self, strategy: Strategy):
        self.title = ""
        self.link = ""
        self.message = ""
        self.whiteList = ["www."]
        self.blackList = ["www."]
        self._strategy = strategy
        # TODO - Checks if we can find out more details about the website

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def addWhiteList(self, link):
        self.whiteList.add(link)

    def addBlackList(self, link):
        self.blackList.add(link)

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class StrategyWebsite(Strategy):
    def do_algorithm(self, data: List) -> List:
        return data


class StrategySocial(Strategy):
    def do_algorithm(self, data: List) -> List:
        return data




