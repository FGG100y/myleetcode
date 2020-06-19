#!/usr/bin/env python
# encoding: utf-8

# A - 1; B - 2; ... ; Z - 26.
# Input: 226
# Output: 3. <-- 1. BBF(2, 2, 6), 2. BZ(2, 26), 3. VF(22, 6)


def decode(num):
    s = str(num)
    res = []
    #  lookup = dict(zip(map(str, range(1, 27)), map(chr(range(65, 91)))))
    pass


if __name__ == "__main__":
    num = 22621
    print(decode(num))
