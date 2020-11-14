import pytest

pytestmark = pytest.mark.skip('only template')


def compute(a, b):
    # implement solution here
    return sum((a, b))


# put arguments and expected results here
ARGS_RESULTS = [
    ((1, 25), 26),
    ((42, 250), 292),
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
