from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

from Analysers.Models import AnalysisResult, AnalysisElement
from Analysers.NaiveBayes import NaiveBayes
from DataLayer.DataSetAdapter import DataSetAdapter
from DataLayer.DataSetEntry import SocialMediaDataSetEntry
from Utils.LoggingAspect import logging_aspect


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request, result: AnalysisResult) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any, result: AnalysisResult) -> str:
        if self._next_handler:
            return self._next_handler.handle(request, result)

        return result


class NewsFilterArticleHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO news filtering
        return super().handle(request, result)


class FactCheckArticleHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO fact check analysis
        super().handle(request, result)


class CommonSenseArticleHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO common sense analysis
        super().handle(request, result)


class InductiveArticleHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO inductive analysis
        super().handle(request, result)

class NewsFilterSocialMediaHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: SocialMediaDataSetEntry, result: AnalysisResult) -> str:
        adapter = DataSetAdapter()
        fit_data, fit_labels = adapter.convert_to_training_datasets()
        bayes = NaiveBayes()
        bayes.fit(fit_data, fit_labels)
        predict_data = adapter.convert_to_predict_data(request)
        predict_result = bayes._predict(predict_data)
        if predict_result == 1:
            result.add_element(AnalysisElement(1, "The provided post is news"))
            return super().handle(request, result)
        else:
            result.add_element(AnalysisElement(0, "The provided post is NOT news"))


class FactCheckSocialMediaHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO fact check analysis
        super().handle(request, result)


class CommonSenseSocialMediaHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO common sense analysis
        super().handle(request, result)


class InductiveSocialMediaHandler(AbstractHandler):
    @logging_aspect
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO inductive analysis
        super().handle(request, result)
