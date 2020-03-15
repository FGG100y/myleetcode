#!/usr/bin/env python
# encoding: utf-8
# test passline score, make sure 60% students passed the test


def passline(scores, pr=0.6):
    """return the passline of the test scores
    :type scores: list
    :rype int
    """
    above60 = [True if s-60 >= 0 else False for s in scores]
    if all(above60):
        return 60
    else:
        idx = int(len(scores) * (1 - pr))
        pl = sorted(scores)[idx]
        return pl // 10 * 10


if __name__ == "__main__":
    scores = [10, 76, 90, 66, 89, 59, 89, 99, 12, 50]
    s = [41] * 10
    print(s)
    print(passline(s))
