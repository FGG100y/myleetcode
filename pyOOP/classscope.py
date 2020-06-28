#!/usr/bin/env python
# encoding: utf-8

# Class in Nested Function
# The lookup rules for 'simple' names like 'X' never search enclosing "class"
# statements -- just "def"s, modules, and built-ins
# (it's the LEGB rule, not CLEGB!)

# We'll see use cases for this nested classes coding pattern later, especially
# in some of "decorators". In this role, the enclosing function usually both
# serves as a class factory and provides retained state for later use in the
# enclosed class or its methods.


X = 1


def nester():
    X = 2                   # Hides global
    print(X)                # Local: 2
    class C:
        X = 3               # Class local hides nester's
        print(X)            # Local: 3
        def m1(self):
            print(X)        # In enclosing def (not 3 in class!): 2
            print(self.X)   # Inherited class local: 3
        def m2(self):
            X = 4           # Hides enclosing (nester, not class)
            print(X)        # Local: 4
            self.X = 5      # Hides class
            print(self.X)   # Located in instance: 5
    I = C()
    I.m1()
    I.m2()


if __name__ == "__main__":
    print(X)                # Global: 1
    nester()                # Rest: 2, 3, 2, 3, 4, 5
