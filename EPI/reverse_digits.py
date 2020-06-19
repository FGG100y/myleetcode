"""Reverse the integer in digits. E.g., input 42, output 24, -312 -> -213
"""


# Let the input be k. If K >= 0, then k mod 10 is the most signigicant digit of
# the result and the subsequent digits are the reverse of k/10.
def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


# Bonus
def palindrome(x):
    if x < 0:
        return False
    else:
        return x == reverse(x)


if __name__ == "__main__":
    x = 1245
    print(reverse(x))
    x = 1221
    print(palindrome(x))
