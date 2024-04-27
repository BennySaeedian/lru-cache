from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Any, NewType
from functools import wraps

from src import DoublyLinkedList
from src.node import Node

# return value from the user's function being cached
FuncReturnValue = NewType("FuncReturnValue", Any)


@dataclass
class CacheKey:
    """
    used to hash args and kwargs of a function to a hashable key
    makes the reasonable assumption that the function args and kwargs are hashable
    """
    args_tuple: tuple[Any, ...]  # (arg1, arg2, ...)
    kwargs_tuple: tuple[tuple[str, Any], ...]  # ( (kwarg_str1, value1), (kwarg_str2, value2), ...)

    def __hash__(self) -> int:
        return hash((self.args_tuple, self.kwargs_tuple))

    @classmethod
    def from_args_kwargs(cls, *args: tuple, **kwargs: dict) -> CacheKey:
        return cls(
            args_tuple=args,
            kwargs_tuple=tuple(sorted(kwargs.items()))
        )


class lru_cache:
    """
    least recently used cache decorator, written as a class
    because decorator functions with arguments are a mess
    """

    def __init__(self, max_size: int | None) -> None:
        """
        if maxsize is None, the cache can grow without bound
        """
        self._max_size: int | None = max_size
        self._recent_return_vals: DoublyLinkedList[FuncReturnValue] = DoublyLinkedList()
        self._cache: dict[CacheKey, Node[FuncReturnValue]] = {}

    def __call__(self, user_func: Callable) -> Callable:
        @wraps(user_func)
        def wrapper(*args, **kwargs) -> FuncReturnValue:
            cache_key = CacheKey.from_args_kwargs(*args, **kwargs)

            return (
                self._on_cache_hit(cache_key)
                if cache_key in self._cache else
                self._on_cache_miss(user_func, args, kwargs, cache_key)
            )

        # attach clear cache functionality
        wrapper.clear_cache = lambda: self.__init__(self._max_size)
        return wrapper

    @property
    def is_bounded(self) -> bool:
        return self._max_size is not None

    def _on_cache_hit(self, cache_key: CacheKey) -> FuncReturnValue:
        node = self._cache[cache_key]
        # move this node to the head of the lru list
        self._recent_return_vals.make_head(node)
        return node.data

    def _on_cache_miss(
            self,
            user_func: Callable,
            args: tuple,
            kwargs: dict,
            cache_key: CacheKey
    ) -> FuncReturnValue:
        self._recent_return_vals.prepend(user_func(*args, **kwargs))
        node = self._recent_return_vals.head
        self._cache[cache_key] = node
        # evict if needed
        if self.is_bounded and len(self._recent_return_vals) > self._max_size:
            self._evict_lru()
        return node.data

    def _evict_lru(self):
        tail = self._recent_return_vals.tail
        # remove the node from the cache dict
        tail_key = [key for key, node in self._cache.items() if node == tail].pop()
        del self._cache[tail_key]
        self._recent_return_vals.remove_node(tail)
