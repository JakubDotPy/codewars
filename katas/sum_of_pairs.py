# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is sum_of_pairs.py                                                #
#  Date: 14.11.20 23:56                                                        #
# ##############################################################################

import pytest

pytestmark = pytest.mark.skip('already solved')

"""Given a list of integers and a single sum value, return the first two values (parse from the left please) in order 
of appearance that add up to form the sum. """


def compute(num_list, sum_val):
    complements = set()
    for num in num_list:
        if num in complements:
            return [sum_val - num, num]
        complements.add(sum_val - num)
    return None


# put arguments and expected results here
ARGS_RESULTS = [
    (([11, 3, 7, 5], 10), [3, 7]),
    (([4, 3, 2, 3, 4], 6), [4, 2]),
    (([0, 0, -2, 3], 2), None),
    (([10, 5, 2, 3, 7, 5], 10), [3, 7])
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
