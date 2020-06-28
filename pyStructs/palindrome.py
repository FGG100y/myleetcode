#!/usr/bin/env python
# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
# E.g., "A man, a plan, a canal: Panama"

# O(n) runtime, O(1) space


def solution(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


if __name__ == "__main__":
    #  string = "A man, a plan, a canal: Panama"
    #  string = 'aba'
    print(solution(s="A man, a plan, a canal: Panama"))
