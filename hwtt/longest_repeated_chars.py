#!/usr/bin/env python
# Input: aaabbbbbcccccccczzzzzzzz
# Output: cccccccc

from collections import defaultdict


def lrchars(s):
    res = defaultdict(int)
    res.setdefault('', 0)
    start, end = 0, 0
    while start < len(s):
        while end <= len(s) and s[start] == s[end]:
            end += 1
            if end >= len(s):
                break
        char = s[start]
        length = end - start
        if length > max(res.values()):
            res[char] = length
        elif length == max(res.values()):
            res[char] = length
        start = end
    result, repeation = '', 0
    for k, v in res.items():
        if v > repeation:
            result, repeation = k, v
    return result*repeation


if __name__ == "__main__":
    s = 'aaabbbbbcccccccczzzzzzzz'
    print(lrchars(s))
