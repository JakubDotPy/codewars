import collections

import pytest


def compute(signature, n):
    """Write the len(signature) nbonci and return first n elements."""
    n_bonaci = len(signature)

    if n < n_bonaci:
        return signature[:n]

    deq = collections.deque(signature, maxlen=n_bonaci)
    res = signature
    while len(res) < n:
        s = sum(deq)
        res.append(s)
        deq.append(s)
    return res


# put arguments and expected results here
ARGS_RESULTS = [
    (([0, 1], 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    (([1, 1], 10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    (([0, 0, 0, 0, 1], 10), [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]),
    (([1, 0, 0, 0, 0, 0, 1], 10), [1, 0, 0, 0, 0, 0, 1, 2, 3, 6]),
    (([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256])
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
