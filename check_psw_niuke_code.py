from collections import defaultdict
import sys


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


def check_ssl(s):
    """return False if len(substring) > 3 && appeared twice
    """
    # while substring's length <= len(s) // 2; do
    # for i in range(), if substring in s, return False
    # else substring's index move one forward, repeat check in
    ssl = 3
    while ssl <= len(s) // 2:
        start, end = 0, ssl
        for i in range(len(s) - ssl*2 + 1):
            if s[start:end] in s[end:]:
                return False
            else:
                start += 1
                end += 1
        ssl += 1
    return True


if __name__ == "__main__":
    try:
        while 1:
            psw = sys.stdin.readline().strip()
            # Be careful, should always do the input's sanity check
            if not psw:
                break
            if check_length(psw) and check_kind(psw) and check_ssl(psw):
                print('OK')
            else:
                print('NG')
    except Exception:
        pass
