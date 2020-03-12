#!/usr/bin/env python
# encoding: utf-8

# In general, an optimization problem has two parts:
# ----------------------------------------------------------------------------
#   * Objective function that is to be maximized or minimized
#
#   * Set of constraints that must be honored
# ----------------------------------------------------------------------------


# 0/1 knapsack problem, which can be formalized as follows:
# ----------------------------------------------------------------------------
#   * each item is represented by a pair, <value, weight>
#
#   * the knapsack has a maximum carried weight of items
#
#   * a vector 'I' of length n, represents  the set of available items
#
#   * a vector 'V' of length n, indicates item taken state, 1:yes, 0:no
#
#   * find a vector V that maximizes the sum of V[i]*I[i].value, and subject
#   to the constraint that the sum of V[i]*I[i].weight <= max_weight_carried
# ----------------------------------------------------------------------------

# NOTE that greedy algorithm will not guaranteed to find an optimal solution
# which runtime of O(n log(n)) while greedy algorithm that guaranteed to find
# the optimal solution which ran in exponential time.

# Fortunately, Dynamic programming provides a practical method for solving 0/1
# knapsack problems in a reasonable amount of time.
# The key idea is to think about exploring the space of possible solutions by
# constructing a rooted binary tree that enumerates all states that satisfy the
# weight constraint.

# A 'rooted binary tree' is an acyclic directed graph in which:
# ----------------------------------------------------------------------------
#   * there is exactly one node with no parents, so called the 'root'
#   * each non-root node has exactly one parent
#   * each node has at most two children, a childless node is called a 'leaf'
# ----------------------------------------------------------------------------
# Each node in the search tree is labeled with a quadruple <{}, [a,b,c], 0, 5>
# which means that {}:no item have been taken, [a, b, c]:all items remain to be
# considered, 0:the value of items taken is 0, and a weight of 5 is still
# available.


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"<{self.name}, {self.value}, {self.weight}>"

    # Calling string on a python list calls the __repr__ method on each
    # element inside, or there will be the address of object which was printed
    def __repr__(self):
        return self.__str__()


# STILL NOT FULLY UNDERSTANT THIS PROGRAM YET. Thu 12 Mar 2020 22:43:20
def fast_maxval(to_consider, avail, memo={}):
    """Dynamic programming solution to knapsack problem

    :type to_consider: list of Items
    :type avail: int
    :type memo: dict
    :rtype tuple
    """
    # use tuple as memo's key to store the sub-problem result
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, [])
    # when the current item's weight exceeded the available weight, check next
    elif to_consider[0].get_weight() > avail:
        # explore right branch only: to_consider[1:] keep rm the first item
        result = fast_maxval(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        # explore rooted tree's left branch: means take the current item
        still_avail = avail - next_item.get_weight()
        with_val, with_take = fast_maxval(to_consider[1:], still_avail, memo)
        with_val += next_item.get_value()
        # explore right branch
        without_val, without_take = fast_maxval(to_consider[1:], avail, memo)
        # choose better branch
        if with_val > without_val:
            result = (with_val, with_take+[next_item])
        else:
            result = (without_val, without_take)
    memo[(len(to_consider), avail)] = result
    return result


def test_fast_maxval(max_weight=100):
    items = build_items()
    result = fast_maxval(items, max_weight)
    print(result)


def build_items():
    names = list(map(chr, range(97, 123)))
    values = list(range(10, 261, 10))
    weights = list(range(26, 53))
    items = [Item(names[i], values[i], weights[i]) for i in range(len(names))]
    return items


if __name__ == "__main__":
    test_fast_maxval()
    #  items = [Item('test', i, 1111) for i in range(4)]
    #  print(items)
