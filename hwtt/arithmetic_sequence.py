#!/usr/bin/env python
# 在等差数列中，任何相邻两项的差相等，该差值称为公差（common difference）。
# 一个等差数列的和，等于其首项与末项的和，乘以项数除以2。


def is_arithmetic_sequence(sequence):
    seq = sorted(sequence.strip().split())
    if ((int(seq[0]) + int(seq[-1])) * len(seq) / 2) == sum(map(int, seq)):
        return 'yes'
    else:
        return 'no'


if __name__ == "__main__":
    seq = '1 3 5 4'
    print(is_arithmetic_sequence(seq))
