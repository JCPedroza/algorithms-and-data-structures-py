from typing import Any


class Queue:
    """Implements a queue using native lists."""

    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        return str(self.list)

    def __len__(self) -> int:
        return len(self.list)

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue.
        :param item: Item to be added to queue.
        """
        self.list.append(item)

    def dequeue(self) -> Any:
        return self.list.pop(0)

    def peek(self) -> Any:
        return self.list[0]

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self) -> None:
        self.list = []


structure = Queue
name = "queue native list"
