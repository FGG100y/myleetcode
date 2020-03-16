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


def find_root(x, power, epsilon=0.001):
    # polynomial: x**power - 12 = 0
    if x < 0 and power % 2 == 0:
        return None
    guess = x / 2.0
    while abs(guess**power - x) >= epsilon:
        try:
            guess -= (guess**power - x) / (power*(guess**(power - 1)))
        except Exception as e:
            raise e

    return guess


# ----------------------------------------------------------------------------
def _first_derivative():
    # polynomial: x**3 + x - 12 = 0
    pass


# seems there is no obvious solution to program this out
def find_poly_root(x, degrees, epsilon=0.001):
    """return y such that polynomial(y) is within epsilon of x
    :type x: numeric
    :type degrees: tuple of ints that represent polynomial degrees, high to low
    :type epsilon: numeric
    :rtype float
    """
    # polynomial: x**3 + x - 12 = 0
    # no solution:

    pass
# ----------------------------------------------------------------------------


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


def find_root_bs(x, power, epsilon=0.001):
    """return y such that y**power is within epsilon of x | binary search
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
    num = 8
    power = 3
    print(square_root(num))
    print(find_root(num, power=power))
    print('*'*11)
    print(square_root_bs(num))
    print(find_root_bs(num, power=power))
