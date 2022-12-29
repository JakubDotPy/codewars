import statistics
from datetime import timedelta

import pytest


def compute(times: str):
    if not str:
        return ''

    d_h_s = lambda td: (td.seconds // 3600, (td.seconds // 60) % 60, td.seconds % 60)

    times_tup = [
        tuple(map(int, s.split('|'))) for s in times.split(', ')
    ]
    deltas_seconds = sorted(
        timedelta(hours=h, minutes=m, seconds=s).total_seconds()
        for h, m, s in times_tup
    )
    _range_seconds = int(deltas_seconds[-1] - deltas_seconds[0])
    _mean_seconds = int(statistics.mean(deltas_seconds))
    _median_seconds = int(statistics.median(deltas_seconds))

    return "Range: {:02}|{:02}|{:02} Average: {:02}|{:02}|{:02} Median: {:02}|{:02}|{:02}".format(
        *d_h_s(timedelta(seconds=_range_seconds)),
        *d_h_s(timedelta(seconds=_mean_seconds)),
        *d_h_s(timedelta(seconds=_median_seconds))
    )


# put arguments and expected results here
ARGS_RESULTS = [
    (("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17",), "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"),
    (("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41",),
     "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00"),
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
