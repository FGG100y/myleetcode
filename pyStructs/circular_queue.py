"""Queue implementation with circularly linked list
"""


class Empty(Exception):
    pass


class CircularQueue:
    """FIFO Queue implementation using a circularly linked list for storage
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
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        # in circularly linked list, tail.next is head
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            # new node points to the head
            newest._next = self._tail._next
            # old tail points to new node
            self._tail._next = newest
        # updage reference ot the tail
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            # old head becomes new tail
            self._tail = self._tail._next
