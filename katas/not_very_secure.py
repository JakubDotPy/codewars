# ##############################################################################
#  This solution for codewars kata was written by Jakub Cervinka.              #
#  Kata name is not_very_secure.py                                             #
#  Date: 15.11.20 0:09                                                         #
# ##############################################################################

import re

import pytest

pytestmark = pytest.mark.skip('already solved')

"""In this example you have to validate if a user input string is alphanumeric. The given string is not 
nil/null/NULL/None, so you don't have to check that. 

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""


def compute(password):
    pattern = re.compile(r'\w+')
    matches = re.fullmatch(pattern, password)
    return bool(matches)


# put arguments and expected results here
ARGS_RESULTS = [
    (('hello world_',), False),
    (('PassW0rd',), True),
    (('     ',), False)
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
