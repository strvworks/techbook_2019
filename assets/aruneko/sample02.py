from typing import TypeVar


A = TypeVar('A', bound=None)


def my_sum(x: A, y: A) -> A:
    return x + y


result1 = my_sum(1, 2)
result2 = my_sum([1, 2], [3, 4])
