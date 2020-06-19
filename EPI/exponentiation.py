"""Compute x**y with x a double, y a integer
"""


# Generalizing, if the least signigicant bit of y is 0, the result is
# (x**(y/2))**2; otherwise, it is x * (x**(y/2))**2.
# The only change when y is negative is replacing x by 1/x and y by -y.
def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


if __name__ == "__main__":
    print(power(2, -3))
