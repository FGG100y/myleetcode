#!/usr/bin/env python
# check the password
# password contains letters, digits, other characters, at least three of them
# appeared and length > 8
from collections import defaultdict


def check_length(s):
    return len(s) > 8


def check_kind(s):
    total = defaultdict(int)
    for c in s:
        if c.isupper():
            if not total['upper']:
                total['upper'] += 1
        elif c.islower():
            if not total['lower']:
                total['lower'] += 1
        elif c.isdigit():
            if not total['digit']:
                total['digit'] += 1
        else:
            if not total['others']:
                total['others'] += 1
    res = sum(total.values())
    return True if res >= 3 else False


def check_ssr(s):
    """return False if len(substring) > 3 && appeared twice
    """
    # while substring's length(ssl) <= len(s) // 2; do
    # for substring in s, if substring in s, return False
    # else substring's index move one forward, repeat check in
    ssl = 3
    while ssl <= len(s) // 2:
        start, end = 0, ssl
        for i in range(len(s) - ssl*2 + 1):
            print(s[start:end])
            if s[start:end] in s[end:]:
                return False
            else:
                start += 1
                end += 1
        ssl += 1
    return True


def check_password(s):
    return 'ok' if check_length(s) and check_kind(s) and check_ssr(s) else 'ng'


if __name__ == "__main__":
    #  s = '021Abc9000'
    s = '021Abc9Abc1'
    print(check_password(s))
