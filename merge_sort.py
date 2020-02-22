#!/usr/bin/env python
# Big O | O(nlog(n)) time complexity


# Merge sort: A Prototypical Divide-and-Conquer algorithm
# * a threshold input size, a.k.a, the 'recursive base'
# * the size and number of sub-instances
# * the algorithm to combine sub-solutions

# merge sort described recursively:
# * if the list is of length 0 or 1, it is already sorted
# * if the list has more than one element, split the list into two lists, and
#   use merge sort to sort each of them
# * merge the results


def merge(left, right, compare):
    """returns a new sorted (by compare method) list containing the same
    elements as (left + right) would contain.

    :type left: list
    :type right: list
    :rtype list
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # only if len(left) > len(right)
    while (i < len(left)):
        result.append(left[i])
        i += 1
    # only if len(left) < len(right)
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L, compare=lambda x, y: x < y):
    """returns new sorted list with the same elements as L
    :type L: list
    :type compare: lambda function
    """
    if len(L) < 2:
        return L[:]
    else:  # split the L into lists whose length < 2, recursion stop
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)
