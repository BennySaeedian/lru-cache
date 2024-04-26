import pytest

from src import *


def test_list_init(linked_list: DoublyLinkedList) -> None:
    assert linked_list.head is linked_list.tail is None
    assert len(linked_list) == linked_list.size == 0


def test_list_append(linked_list: DoublyLinkedList) -> None:
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert len(linked_list) == 3
    assert list(linked_list) == [1, 2, 3]


def test_list_prepend(linked_list: DoublyLinkedList) -> None:
    linked_list.prepend('c')
    linked_list.prepend('b')
    linked_list.prepend('a')
    assert len(linked_list) == 3
    assert list(linked_list) == ['a', 'b', 'c']


def test_list_remove_node(list_with_data: DoublyLinkedList) -> None:
    zero_node = list_with_data.head
    two_node = zero_node.next_node.next_node
    four_node = list_with_data.tail
    list_with_data.remove_node(two_node)
    assert len(list_with_data) == 4
    assert list(list_with_data) == [0, 1, 3, 4]
    list_with_data.remove_node(zero_node)
    assert list(list_with_data) == [1, 3, 4]
    list_with_data.remove_node(four_node)
    assert list(list_with_data) == [1, 3]
    list_with_data.remove_node(list_with_data.head)
    assert list(list_with_data) == [3]
    list_with_data.remove_node(list_with_data.head)
    assert len(list_with_data) == 0
    assert list(list_with_data) == []


def test_list_remove_data(list_with_duplicates: DoublyLinkedList) -> None:
    list_with_duplicates.remove_data(1)
    assert len(list_with_duplicates) == 4
    assert list(list_with_duplicates) == [1, 1, 1, 1]
    list_with_duplicates.remove_data(data=1, count=4)
    assert list(list_with_duplicates) == []
    with pytest.raises(ValueError):
        list_with_duplicates.remove_data(1)


def test_list_make_head(list_with_data: DoublyLinkedList) -> None:
    four_node = list_with_data.tail
    list_with_data.make_head(four_node)
    assert list(list_with_data) == [4, 0, 1, 2, 3]
    list_with_data.make_head(four_node)
    assert list(list_with_data) == [4, 0, 1, 2, 3]
    zero_node = list_with_data.head.next_node
    list_with_data.make_head(zero_node)
    assert list(list_with_data) == [0, 4, 1, 2, 3]
    two_node = list_with_data.tail.prev_node
    list_with_data.make_head(two_node)
    assert list(list_with_data) == [2, 0, 4, 1, 3]
    list_with_data.make_head(list_with_data.tail)
    assert list(list_with_data) == [3, 2, 0, 4, 1]
