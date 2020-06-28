"""The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0.
"""


# brute-force solution, O(n), n is the length of bits
def parity1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# O(k), k is the bits set of 1 in the word x
def parity2(x):
    result = 0
    while x:
        result ^= 1
        # drop the lowest set bit of x
        x &= x - 1
    return result


# NOTE that XOR of two bits is defined to be 0 if they are the same, otherwise
# it is 0. And the XOR of a group of bits is its parity. E.g., the parity of
# <b63, b62, ..., b2, b1, b0> equals the parity of the XOR of <b63, b62, ...,
# b32> and <b31, b30, ..., b0>.
def parity3(x):  # O(log(n)), n is the word size
    # assumes x is 64-bits
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == "__main__":
    x = 15
    print(bin(x))
    print(parity1(x))
    print(parity2(x))
    print(parity3(x))
