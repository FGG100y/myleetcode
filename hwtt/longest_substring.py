#!/usr/bin/env python
# encoding: utf-8


def longest_substring(s):
    # start, end to keep tracking the current substring
    # 'end' begin at index i=0, move forword, if  a second char at index j,
    # store the candidate lss=s[i:j], iff len(lss) < j-i+1, update the lss
    # then, update index i to i+1, and keep searching forword
    lookup = set()
    i, j = 0, 0
    while j <= len(s):
        if j == len(s):  # due to the string slice nature
            lookup.add(s[i:])
            break
        while s[j] in s[i:j]:
            print('*', s[i:j])
            lookup.add(s[i:j])
            i += 1
        j += 1
    lss = ''
    for s in lookup:
        if len(lss) < len(s):
            lss = s
    print('='*len(lss))
    return lss


if __name__ == "__main__":
    s = 'askkkkkksl,'
    print(s)
    print('='*len(s))
    print(longest_substring(s))
