#!/usr/bin/env python
# filter repeated characters


def filter_chars(s):
    # return unique characters string
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res


if __name__ == "__main__":
    print(filter_chars('bacaadcae'))
