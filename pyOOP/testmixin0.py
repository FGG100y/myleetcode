#!/usr/bin/env python
# get ListInstance's __str__ 'for free'
from mixins_listinstance import ListInstance


class Super:
    """description"""
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInstance):
    """description"""
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


if __name__ == "__main__":
    X = Sub()
    print(X)
