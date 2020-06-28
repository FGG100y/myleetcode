"""Stack implementation with singly linked list
"""
# NOTE that __slots__ Declaration is a more direct mechanism for representing
# instance namespaces that avoids the use of an auxiliary dictionary. To use
# the streamlined representation for all instances of a class, that class
# difinition must provide a class-level member named __slots__ that is assigned
# to a fixed sequence of strings that serve as names for instance variables.
#
# When inheritance is used, if the base class declares __slots__, a subclass
# must also declare __slots__ to avoid creation of instance dictionaries. The
# declaration in the subclass should only include names of supplemental methods
# that are newly introduced.
#
# To promote greater efficiency in memory usage, we will use an explicit
# __slots__ declaration lin any nested classes for which we expect many
# instances.


class Empty(Exception):
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage
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

    # stack methods
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """Remove and return the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
