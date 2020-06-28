"""LIFO Stack implementation using a Python list as underlying storage
"""


class Empty(Exception):
    # to produce appropriate Error Msg for misbehave operations on Stack
    pass


class ArrayStack:
    # using Python list as container
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top to the stack"""
        self._data.append(e)

    def top(self):
        """Return (but not remove) the element at the top of stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()