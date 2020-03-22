#!/usr/bin/env python
# input: 12336544
# output: 456321
# input: 1750
# output: 571
# input: -342
# output: -243


def drop_duplicate(s):
    res = ''
    for c in s:
        if (c not in res):
            res += c
    return res


def reverse_string(s):
    return s[1:][::-1] if s[0] == '-' else s[::-1]


def func(s):
    sign = s[0] if s[0] == '-' else ''
    while s[-1] == '0':
        s = s[:-1]
    rvs = reverse_string(s)
    dds = drop_duplicate(rvs)
    return sign+dds


if __name__ == "__main__":
    s = str(-12336504400)
    print(func(s))
