#!/usr/bin/env python
# binary search algorithm


def bsearch_recursion(L, e):
    """
    :type L: list which elements in ascending order
    :type e: oject which in L
    :rtype boolean
    """

    # helper function to perform recursion
    def bsearch(L, e, low, high):
        # decrements the high and low
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bsearch(L, e, low, mid - 1)
        else:
            return bsearch(L, e, mid + 1, high)

    # where function begin
    if len(L) == 0:
        return False
    else:
        return bsearch(L, e, 0, len(L) - 1)
