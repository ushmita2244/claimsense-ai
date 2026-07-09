import time

from core.utils.timer import Timer


def test_timer_measures_elapsed_time():
    """
    Timer should measure elapsed execution time.
    """

    with Timer() as timer:
        time.sleep(0.1)

    assert timer.elapsed >= 0.1