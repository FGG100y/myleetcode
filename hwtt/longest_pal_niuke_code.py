# import sys


def xcenter(s, left, right):
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def longest_pal(s):
    """counts the length of the longest palindrome in a string
    """
    start, end = 0, 0
    for i in range(len(s)):
        # len(s) is odd
        len1 = xcenter(s, i, i)
        # len(s) is even
        len2 = xcenter(s, i, i + 1)
        len_max = max(len1, len2)
        if len_max > end - start:
            # 'distance' between start and center
            start = i - (len_max - 1) // 2
            # 'distance' between end and center
            end = i + len_max // 2

    return len(s[start:end+1])


if __name__ == "__main__":
    try:
        while 1:
            # should know when to use sys.stdin.readline(s) and when not
            s = input()
            print(longest_pal(s))
    except:
        pass
