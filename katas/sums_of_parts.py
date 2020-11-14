# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is sums_of_parts.py                                               #
#  Date: 15.11.20 1:00                                                         #
# ##############################################################################

import pytest

pytestmark = pytest.mark.skip('already solved')

"""
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of 
the sums of its parts as defined above. """


def compute(nums):
    total = sum(nums)
    result = [total]
    for num in nums:
        total -= num
        result.append(total)
    return result


# put arguments and expected results here
ARGS_RESULTS = [
    (([0, 1, 3, 6, 10],), [20, 20, 19, 16, 10, 0]),
    (([1, 2, 3, 4, 5, 6],), [21, 20, 18, 15, 11, 6, 0]),
    (([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358],),
     [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]),
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
