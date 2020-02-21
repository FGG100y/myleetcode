#!/usr/bin/env python
# Time:  O(n)
# Space: O(1)

# Given two non-negative numbers num1 and num2 represented as string,
# return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or
# convert the inputs to integer directly.


def solution(n1, n2):
    result = []
    i, j, carry = len(n1) - 1, len(n2) - 1, 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += ord(n1[i]) - ord('0')
            i -= 1
        if j >= 0:
            carry += ord(n2[j]) - ord('0')
            j -= 1
        result.append(str(carry % 10))
        carry /= 10
    result.reverse()

    return "".join(result)


def solution2(n1, n2):
    length = max(len(n1), len(n2))
    n1 = n1.zfill(length)[::-1]
    n2 = n2.zfill(length)[::-1]
    res, plus = '', 0
    for idx, val in enumerate(n1):
        temp = str(int(val) + int(n2[idx]) + plus)
        res += temp[-1]
        if int(temp) > 9:
            plus = 1
        else:
            plus = 0
    if plus:
        res += '1'
    return res[::-1]


if __name__ == "__main__":
    print(solution("89", "3544"))
    print(solution2("1", "3"))
