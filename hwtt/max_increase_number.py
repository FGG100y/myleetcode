#!/usr/bin/env python
# Input: 123526897215, the increasing numbers includs: 1235, 2689, 15
# Output: 2689, the maximum one


def max_num(n):
    results = set()
    s = str(n)
    k, i, j = 0, 0, 1
    while k < len(s):
        #  while j <= len(s) and int(s[i]) <= int(s[j]):
        while j <= len(s) and int(s[i]) < int(s[j]):  # strict increased num
            #  res += s[i]
            j += 1
            i += 1
            if j >= len(s):
                break
        res = s[k:j]
        results.add(res)
        print(results)
        k = j
        j += 1
        i += 1
    mx = 0
    for m in results:
        if int(m) > mx:
            mx = int(m)
    return mx


if __name__ == "__main__":
    n = 126226897815
    print(max_num(n))
