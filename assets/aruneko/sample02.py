from typing import List, TypeVar

A = TypeVar('A')


def head(xs: List[A]) -> A:
    return xs[0]


result1 = head([1, 2, 3, 4, 5])
result2 = head(['a', 'b', 'c'])
