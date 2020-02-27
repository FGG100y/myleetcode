#!/usr/bin/env python
# Big O | logarithmic complexity


def int2str(i):
    """returns a decimal string representation of an int
    :type i: int
    :rtype str
    """
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i //= 10
    return result


def add_digits(n):
    """returns the sum of the digits in a nonnegative int
    :type n: int
    :rtype int
    """
    str_reps = int2str(n)
    val = 0
    for c in str_reps:
        val += int(c)
    return val
