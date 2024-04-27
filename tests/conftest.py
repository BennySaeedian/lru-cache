from typing import Callable

import pytest

from src import lru_cache
from src.doubly_linked_list import DoublyLinkedList


@pytest.fixture
def linked_list() -> DoublyLinkedList:
    return DoublyLinkedList()


@pytest.fixture
def list_with_data() -> DoublyLinkedList:
    list_ = DoublyLinkedList()
    for i in range(5):
        list_.append(i)
    return list_


@pytest.fixture
def list_with_duplicates() -> DoublyLinkedList:
    list_ = DoublyLinkedList()
    for _ in range(5):
        list_.append(1)
    return list_


@pytest.fixture
def cached_printer_function() -> Callable:
    @lru_cache(max_size=3)
    def cached_printer(*args, **kwargs):
        print(f"{args=} {kwargs=}", end='')
        return args, kwargs

    return cached_printer
