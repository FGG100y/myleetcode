"""Generate uniform random numbers by using a random number generator that
produces zero or one with equal probability.
"""
import random


# NOTE that it is easy to produces random integer between 0 and (2**i - 1) by
# concatenating i bits producesd by the random number generator.
# For generally speaking, first note that it is equivalent to produce a random
# integer between 0 and (b - a), inclusive, since we can simply add a to the
# result.
# But if (b - a) is not of the form (2**i - 1), we must find the smallest
# number of the form (2**i - 1) that is greater than (b - a). And if the
# Generated i-bit number is not within the range [0, b-a], we try again with i
# new random bits, and keep trying until we get a number within the range.
def uniform_random(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | random.choice([0, 1])
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


if __name__ == "__main__":
    for i in range(10):
        print(uniform_random(10, 19), end=" ")
