import datetime
from contextlib import contextmanager
from time import sleep, perf_counter
import time


def waiter():
    for i in range(1, 3):
        sleep(i)


class cm_timer_2(object):
    def __enter__(self):
        self.t = time.clock()
        return self

    def __exit__(self, type, value, traceback):
        self.t = time.clock() - self.t


@contextmanager
def cm_timer_1() -> float:
    start = perf_counter()
    yield lambda: perf_counter() - start


def main():
    with cm_timer_1() as t:
        sleep(2)
    print(t())
