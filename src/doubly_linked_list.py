from typing import Generic, TypeVar, Iterator

from src.node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    """
    generic doubly linked list
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
        # used for iterations
        self._current = None

    def __repr__(self) -> str:
        node_reprs = [str(node) for node in self]
        nodes_chain_repr = " <--> ".join(node_reprs)
        return f"DoublyLinkedList({nodes_chain_repr})"

    def __iter__(self) -> Iterator[T]:
        """
        initializes the linked list as an iterator
        and returns it
        """
        self._current = self._head
        return self

    def __next__(self) -> T:
        if self._current is None:
            raise StopIteration()
        current_data = self._current.data
        self._current = self._current.next_node
        return current_data

    def __len__(self) -> int:
        return self._size

    @property
    def head(self) -> Node:
        return self._head

    @property
    def tail(self) -> Node:
        return self._tail

    @property
    def size(self) -> int:
        return self._size

    def append(self, data: T) -> None:
        """
        appends a new node to the end of the linked list, the tail
        """
        new_node = Node(
            data=data,
            next_node=None,
            prev_node=self._tail,
        )
        # if the linked list is empty, the tail and head should be the new node
        if self._size == 0:
            self._head = new_node
        # else, a tail exists, we need to set its pointer
        else:
            self._tail.next_node = new_node
        # finally, set the new node as the tail
        self._tail = new_node
        self._size += 1

    def prepend(self, data: T) -> None:
        """
        prepends a new node the start of the linked list, the head
        """
        new_node = Node(
            data=data,
            next_node=self._head,
            prev_node=None,
        )
        # if the linked list is empty, the tail and head should be the new node
        if self._size == 0:
            self._tail = new_node
        # else a head exists, we need to set its pointer
        else:
            self._head.prev_node = new_node
        # finally, set the new node as the head
        self._head = new_node
        self._size += 1
