#!/usr/bin/env python
# general version of testmixin0.py
"""Generic lister mixin tester: similar to transitive reloader in Chapter 15,
but passes a class object to tester (not function), and testByNames adds
loading of both module and class by name strings here, in keeping with Chapter
31's factories pattern.
"""
import importlib


def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)  # Import by namestring
    listerclass = getattr(modobject, classname)  # Fetch attr by namestring
    tester(listerclass, sept)


if __name__ == "__main__":
    testByNames('mixins_listinstance', 'ListInstance', True)

