#!/usr/bin/env python
# encoding: utf-8

# The 'Zen' of Namespaces: Assignments Classify Names

X = 11                  # Global(module) name/attribute (X, oop_manynames.X)


def f():
    print(X)            # Access global X (11)


def g():
    X = 22              # Local(funciton) variable (X, hides module X)
    print(X)


def g2():
    global X
    X = 22              # Change global in module
    print(X)
    X = 11              # Restore the global X to 11


def h1():
    X = 666             # Local in function
    def nested():
        print(X)        # Reference local in encloing scope (666)


def h2():
    X = 666             # Local in function
    def nested():
        nonlocal X      # Python3.x statement
        X = 777         # Change local in encloing scope


class C:
    X = 33              # Class attribute (C.X)
    def m(self):
        X = 44          # Local variable in method (X)
        self.X = 55     # Instance attribute (instance.X)


if __name__ == "__main__":
    print(X)            # 11: module (a.k.a oop_manynames.X outside file)
    f()                 # 11: global
    g()                 # 11: local
    print(X)            # 11: module name unchanged

    obj = C()           # Make instance
    print(obj.X)        # 33: class name inherited by instance

    obj.m()             # Attach attribute name to instance now
    print(obj.X)        # 55: instance
    print(C.X)          # 33: class (a.k.a obj.X if no X in instance)

    print(C.m.X)        # Fails: only visible in method
    print(g.X)          # Fails: only visible in function
