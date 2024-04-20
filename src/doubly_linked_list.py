from typing import Generic, TypeVar

from src.node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    """
    generic doubly linked list
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data: T) -> None:
        """
        appends a new node to the end of the linked list, the tail
        """
        new_node = Node(
            data=data,
            next_node=None,
            prev_node=self.tail,
        )
        # if the linked list is empty, the tail and head should be the new node
        if self.size == 0:
            self.head = new_node
        # else, a tail exists, we need to set its pointer
        else:
            self.tail.next_node = new_node
        # finally, set the new node as the tail
        self.tail = new_node
        self.size += 1

    def prepend(self, data: T) -> None:
        """
        prepends a new node the start of the linked list, the head
        """
        new_node = Node(
            data=data,
            next_node=self.head,
            prev_node=None,
        )
        # if the linked list is empty, the tail and head should be the new node
        if self.size == 0:
            self.tail = new_node
        # else a head exists, we need to set its pointer
        else:
            self.head.prev_node = new_node
        # finally, set the new node as the head
        self.head = new_node
        self.size += 1
