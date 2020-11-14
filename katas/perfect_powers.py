# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is perfect_powers.py                                              #
#  Date: 15.11.20 0:44                                                         #
# ##############################################################################

import pytest

pytestmark = pytest.mark.skip('already solved')

"""
A perfect power is a classification of positive integers:

In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive 
integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n. 

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with 
mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent. 

Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid 
solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.
"""


# NOTE: stupid bruteforced solution, more clever math solution exists
def compute(num):
    for n in range(2, 1000):
        for k in range(2, 1000):
            res = n ** k
            if res > num:
                break
            if res == num:
                return [n, k]


# put arguments and expected results here
ARGS_RESULTS = [
    ((81,), [3, 4]),
    ((4,), [2, 2]),
    ((9,), [3, 2]),
    ((5,), None),
    ]


@pytest.mark.parametrize(
    ('input_args', 'expected'),
    ARGS_RESULTS,
    )
def test(input_args, expected) -> None:
    assert compute(*input_args) == expected


def main() -> int:
    for args, result in ARGS_RESULTS:
        print(compute(*args))
    return 0


if __name__ == '__main__':
    exit(main())
