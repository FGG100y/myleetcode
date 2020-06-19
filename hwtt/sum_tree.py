#!/usr/bin/env python
# encoding: utf-8

# recursion to visit sublists along the way


def sum_tree(lst=None):
    tot = 0
    for x in lst:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sum_tree(x)
    return tot


# breadth_first fashion: adds nested list's contents to the end of the list,
# forming a 'first-in-first-out' queue.
def sum_tree2(lst):
    tot = 0
    items = list(lst)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


# depth_first fashion: adds the content of nested lists to the front of the
# list, forming a 'last-in-first-out' stack.
def sum_tree3(lst):
    tot = 0
    items = list(lst)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot



if __name__ == "__main__":
    print(sum_tree([1, [2, [3, [4, [5]]]]]))  # Prints 15 (right-heavy)
    print(sum_tree([[[[[1], 2], 3], 4], 5]))  # Prints 15 (left-heavy)
