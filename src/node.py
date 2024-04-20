from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):

    def __init__(
            self,
            data: T,
            next_node: Node[T] | None = None,
            prev_node: Node[T] | None = None,
    ) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self) -> str:
        data = self.data
        return f"Node({data=})"
