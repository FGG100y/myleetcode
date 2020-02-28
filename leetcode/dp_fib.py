#!/usr/bin/env python
# Dynamic Programing version of recursive fibonacci


def fast_fib(n, memo={}):
    """returns Fibonacci of n
    :type n: int
    :type memo: dict
    :rtype int
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result
        return result
