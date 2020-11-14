# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is primes_in_numbers.py                                           #
#  Date: 14.11.20 20:14                                                        #
# ##############################################################################

from collections import Counter

import pytest

pytestmark = pytest.mark.skip('already solved')

"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the 
following form : 

 "(p1**n1)(p2**n2)...(pk**nk)"
where a ** b means a to the power of b

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def primefac(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def compute(num):
    factors = Counter(primefac(num))
    result = ''.join(
        f'({num}**{power})' if power > 1 else f'({num})'
        for num, power in sorted(factors.items(), key=lambda x: x[0])
        )
    return result


# put arguments and expected results here
ARGS_RESULTS = [
    ((86240,), '(2**5)(5)(7**2)(11)'),
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
