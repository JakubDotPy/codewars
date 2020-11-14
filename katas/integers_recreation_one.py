# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is integers_recreation_one.py                                     #
#  Date: 14.11.20 20:16                                                        #
# ##############################################################################


import math

import pytest

pytestmark = pytest.mark.skip('already solved')

"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 
1764. The sum of the squared divisors is 2500 which is 50 * 50, a square! 

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is 
itself a square. 42 is such a number. 

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two 
elements, first the number whose squared divisors is a square and then the sum of the squared divisors.
"""


def divisorGenerator(n):
    """well_established divisor generator"""
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def is_square(num):
    root = math.sqrt(num)
    return int(root + 0.5) ** 2 == num


def compute(m, n):
    results = []
    for num in range(m, n):
        divisors_sum = sum(div * div for div in divisorGenerator(num))
        if is_square(divisors_sum):
            results.append([num, divisors_sum])
    return results


# put arguments and expected results here
ARGS_RESULTS = [
    ((1, 250), [[1, 1], [42, 2500], [246, 84100]]),
    ((42, 250), [[42, 2500], [246, 84100]]),
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
