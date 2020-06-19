"""Find the closest integer with the same weight of x.

Define the weight of a nonnegative integer x to be the number of bits that are
set to 1 in its binary representation. E.g., the weight of 9(0b1001) is 2.
"""


# O(n) solution
def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            # Swap (bit - i) and (bit - (i + 1))
            x ^= (1 << i) | (1 << (i + 1))
            return x
    raise ValueError("All bits are 0 or 1")
