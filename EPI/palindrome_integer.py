"""Check if a integer is a palindrome, e.g., 12321 -> True, 12312 -> False
"""
import math


# The number of digits in the input's string representation is n = log10(x)+1,
# Therefore, the least signigicant digit is x%10, and most signigicant digit
# is x/(10**(n-1)). So we can compare the LSD and MSD and then drop them.
# O(n) runtime, O(1) space
def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask   # remove the most signigicant digit of x
        x //= 10        # remove the least signigicant digit of x
        msd_mask //= 100
    return True


if __name__ == "__main__":
    x = 123213
    print(is_palindrome_number(x))
