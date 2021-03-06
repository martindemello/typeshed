"""Stub file for the '_heapq' module."""

from typing import TypeVar, List, Iterable, Any, Callable, Optional
import sys

_T = TypeVar("_T")

def heapify(heap: List[_T]) -> None: ...
def heappop(heap: List[_T]) -> _T:
    raise IndexError()  # if list is empty
def heappush(heap: List[_T], item: _T) -> None: ...
def heappushpop(heap: List[_T], item: _T) -> _T: ...
def heapreplace(heap: List[_T], item: _T) -> _T:
    raise IndexError()  # if list is empty
if sys.version_info < (3,):
    def nlargest(n: int, iterable: Iterable[_T]) -> List[_T]: ...
    def nsmallest(n: int, iterable: Iterable[_T]) -> List[_T]: ...
