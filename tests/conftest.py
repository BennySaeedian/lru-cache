import pytest

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

