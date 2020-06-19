"""reverse bits using caching technique

For a 64-bits word, we compute the reverse of 4 nonoverlapping groups of
16-bits subword, means we create a 2**16=65536 entries hash table for storing
the reversed subwords (i.e., precompute_reversed), e.g., build an array-based
lookup-table A such that for every 16-bit integer y, A[y] holds the
bit-reversal of y. We can then form the reverse of x with the reverse of y0 in
the most significant bit positions, followed by the reverse of y1, followed by
the y2, followed by the y3.
"""
# 16-bit lookup table
reverse_lookup = {}


def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (reverse_lookup[x & BIT_MASK] << (3 * MASK_SIZE)
            | reverse_lookup[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)
            | reverse_lookup[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | reverse_lookup[(x >> (3 * MASK_SIZE)) & BIT_MASK])
