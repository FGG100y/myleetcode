#!/usr/bin/env python
# encoding: utf-8
# 'xxxbyyyyymm' --> '3xb5y2m'


def compress_string(s):
    # be careful with the last loop
    res = ''
    i, j = 0, 0
    while i < len(s):
        while j <= len(s) and s[i] == s[j]:
            j += 1
            if j >= len(s):
                break
        if j - i == 1:
            res += s[i]
        else:
            res += str(j - i) + s[i]
        #  print(res)
        i = j
    return res


if __name__ == '__main__':
    s = 'xxbxyyyyymm'
    print(s)
    print('*'*len(s))
    print(compress_string(s))
