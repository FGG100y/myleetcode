#!/usr/bin/env python
# Big O | quadratic time complexity


def is_subset(s1, s2):
    """identify if one set is subset of the other
    :type s1, s2: list
    :rtype boolean
    """
    for e1 in s1:
        matched = False
        for e2 in s2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(s1, s2):
    """returns a list without duplicates that is the intersection of s1 and s2
    :type s1: list
    :type s2: list
    :rtype list
    """
    # build a list containing common elements
    tmp = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                tmp.append(e1)
                break
    # drop the duplicates
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result
