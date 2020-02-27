#!/usr/bin/env python
# delete chars in string which appeared the lest
# and perserve the order of lefted chars
from collections import defaultdict


def count_chars(s):
    # using defaultdict to keep char's records
    chars = defaultdict(int)
    for c in s:
        chars[c] += 1
    max_val = 20
    for v in chars.values():
        if v < max_val:
            max_val = v
    min_chars = ''
    for k, v in chars.items():
        if v == max_val:
            min_chars += k
    print('min_chars:', min_chars)
    for c in s:
        if c in min_chars:
            s = s.replace(c, '')
    return s


if __name__ == "__main__":
    s = 'adfjlkjkhh'
    print(s)
    print('-'*len(s))
    print(count_chars(s))
