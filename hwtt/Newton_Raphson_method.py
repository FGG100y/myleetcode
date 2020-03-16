#!/usr/bin/env python
# Newton proved a theorem that implies that if a value, call it 'guess', is an
# approximation to a root of a polynomial, then
#   "guess - poly(guess)/poly'(guess)"
#   where poly' is the first derivative of poly,
# is a better approximation.


def square_root(num, epsilon=0.001):
    """find the square root of an integer using Newton-Raphson method
    :type num: int
    :rtype float
    """
    if num < 0:
        return None
    # polynomial: x**2 - 12 = 0
    tot_steps = 0
    guess = num / 2.0
    while abs(guess*guess - num) >= epsilon:
        guess -= (guess**2 - num) / (2*guess)
        tot_steps += 1

    print(f"Newton-Raphson total steps: {tot_steps}")
    return guess


def square_root_bs(num, epsilon=0.001):
    """find the square root of an integer using binary search
    :type num: int
    :rtype float
    """
    if num < 0:
        return None
    tot_steps = 0
    low, high = 0, max(1.0, num)
    ans = (high + low) / 2.0
    while abs(ans*ans - num) >= epsilon:
        if ans*ans < num:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
        tot_steps += 1

    print(f"binary search total steps: {tot_steps}")
    return ans


def find_root(x, power, epsilon=0.001):
    """return y such that y**power is within epsilon of x
    :type x: numeric
    :type power: int
    :type epsilon: numeric
    :rtype float
    """
    if x < 0 and power % 2 == 0:
        return None
    low, high = min(-1.0, x), max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0

    return ans


if __name__ == "__main__":
    #  num = 0.49
    num = 2.5
    print(square_root(num))
    print(square_root_bs(num))
    print(find_root(num, power=2))
