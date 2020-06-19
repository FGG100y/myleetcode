"""Binary word can be viewed as array of bits, swap bits in i-th and j-th index
only make a different when these bits are different.
"""


# O(1) solution
def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        # swap them by flipping their values (thx to the binary)
        # select the bits to flip with bit_mask. Since x ^ 1 = 0 when x = 1
        # and x ^ 1 = 1 when x = 0, we can perform the flip XOR
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == "__main__":
    x = 123
    print(bin(x))
    print(bin(swap_bits(x, 2, 3)))
