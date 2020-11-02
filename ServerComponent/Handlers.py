from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

from Models import AnalysisResult


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
            return self._next_handler.handle(request,result)

        return None


class NewsFilterHandler(AbstractHandler):
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO news filtering
        return super().handle(request,result)


class FactCheckHandler(AbstractHandler):
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO fact check analysis
        super().handle(request,result)


class CommonSenseHandler(AbstractHandler):
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO common sense analysis
        super().handle(request,result)


class InductiveHandler(AbstractHandler):
    def handle(self, request: Any, result: AnalysisResult) -> str:
        # TODO inductive analysis
        super().handle(request,result)
