import time


class Timer:
    """
    Context manager for measuring execution time.
    """

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.end = time.perf_counter()

        self.elapsed = self.end - self.start