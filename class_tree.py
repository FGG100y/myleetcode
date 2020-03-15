#!/usr/bin/env python
# encoding: utf-8

"""
class_tree.py: Climb inheritance trees using namespace links,
displaying higher superclasses with indentation for height
"""


def class_tree(cls, indent):
    print('.' * indent + cls.__name__)      # Print class name here
    for supercls in cls.__bases__:
        class_tree(supercls, indent+4)      # May visit super > once


def instance_tree(inst):
    print(f'Tree of {inst}')                 # Show instance
    class_tree(inst.__class__, 4)            # Climb to its class


def self_test():
    class A:        pass
    class B(A):        pass
    class C(A):        pass
    class D(B, C):        pass
    class E:        pass
    class F(D, E):        pass
    instance_tree(B())
    instance_tree(F())


if __name__ == "__main__":
    self_test()


#  Tree of <__main__.self_test.<locals>.B object at 0x000002CAEAF3B888>
#  ....B
#  ........A
#  ............object
#  Tree of <__main__.self_test.<locals>.F object at 0x000002CAEAF3B888>
#  ....F
#  ........D
#  ............B
#  ................A
#  ....................object
#  ............C
#  ................A
#  ....................object
#  ........E
#  ............object
