"""Queue implementation with singly linked list
"""


class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage
    """
    # nested _Node class
    class _Node:
        """Lightweight nonpublic class for storing a singly linked list
        """
        # streamline memory usage
        # __slots__ is a Tuple
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # Queue methods
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        # node will be new tail node
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        # update reference to tail node
        self._tail = newest
        # update size
        self._size += 1
