from __future__ import annotations

from typing import Generic, TypeVar, Iterator

from src.node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    """
    generic doubly linked list with support for iteration
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
        # used for iterations
        self._current = None

    def __repr__(self) -> str:
        data_chain_repr = " <--> ".join(map(str, self))
        return f"{self.__class__.__name__}({data_chain_repr})"

    def __iter__(self) -> Iterator[T]:
        """
        initializes the linked list as an iterator
        and returns it
        """
        self._current = self._head
        return self

    def __next__(self) -> T:
        """
        returns the next value in the iteration
        """
        if self._current is None:
            raise StopIteration()
        data = self._current.data
        self._current = self._current.next_node
        return data

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
        return len(self)

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

    def remove_node(self, node: Node[T]) -> None:
        """
        removes the given node from the linked list
        """
        # if we are removing the head, the new head the next node waiting in line
        if node == self._head:
            self._head = node.next_node
        # else, the prev pointer is not null, and we need to fix the pointers
        else:
            node.prev_node.next_node = node.next_node
        # if we are removing the tail, a new tail should be set
        if node == self._tail:
            self._tail = node.prev_node
        # else, node has a next pointer which is not null, and must be dealt
        else:
            node.next_node.prev_node = node.prev_node

        self._size -= 1

    def remove_data(self, data: T, count: int = 1) -> None:
        """
        removes the given value from the linked list
        """
        removals_count = 0
        current_node = self._head
        while current_node and (removals_count < count):
            if current_node.data == data:
                self.remove_node(current_node)
                removals_count += 1
                if removals_count == count: break
            current_node = current_node.next_node

        if removals_count == 0:
            raise ValueError("The given data is not in the linked list")

    def make_head(self, node: Node[T]) -> None:
        """
        moves the given node to be the new head of the linked list
        """
        if node == self._head:
            return
        # if the node is the head it has a prev node, adjust it pointers
        node.prev_node.next_node = node.next_node
        # if the node being moved is the tail, a new tail is needed
        if node == self._tail:
            self._tail = self.tail.prev_node
        # if the node is the tail it has a next node, adjust it pointers
        else:
            node.next_node.prev_node = node.prev_node
        # place the node as head
        node.next_node = self._head
        self._head.prev_node = node
        node.prev_node = None
        self._head = node
