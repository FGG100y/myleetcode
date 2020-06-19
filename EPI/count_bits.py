"""count number of bits that are set to 1 in a positive integer
"""


def count_bits(x):
    total = 0
    while x:
        total += x & 1
        x >>= 1
    return total


# parity means the number of set bit is odd
def parity(x):
    # NOTE that x & (x - 1) equals x with its lowest 'set bit' erased
    result = 0
    while x:
        print(bin(x))
        result ^= 1
        x &= x - 1
    return result


if __name__ == "__main__":
    x = 31
    #  print(count_bits(x))
    print(parity(31))
