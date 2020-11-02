from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class OrderIterator(Iterator):

    _position: int = None

    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class SentencesCollections(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> OrderIterator:
        return OrderIterator(self._collection)

    def add_sentence(self, item: Any):
        self._collection.append(item)