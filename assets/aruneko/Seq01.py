from typing import Callable, TypeVar, Generic, List

from functionalpy.Monad import Monad

A = TypeVar('A')
B = TypeVar('B')


class Seq(list, Monad,  Generic[A]):
    def __init__(self, *values: List[A]) -> None:
        super().__init__(values)

    # Functor
    def map(self, f):
        # type: (Callable[[A], B]) -> Seq[B]
        pass

    # Applicative
    def ap(self, fs):
        # type: (Seq[Callable[[A], B]]) -> Seq[B]
        pass

    # Monad
    def flat_map(self, f):
        # type: (Callable[[A], Seq[B]]) -> Seq[B]
        pass
