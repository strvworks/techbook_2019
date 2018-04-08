import unittest
from functionalpy import Seq


def test_monad_1st_low(self):
    seq = Seq(1)

    def f(x):
        return Seq(x + 1)

    self.assertEqual(seq.flat_map(f), f(1))


def test_monad_2nd_low(self):
    seq = Seq(1, 2, 3, 4, 5)

    self.assertEqual(seq.flat_map(Seq), seq)


def test_monad_3rd_low(self):
    seq = Seq(1, 2, 3, 4, 5)

    def f(x):
        return Seq(x + 1)

    def g(x):
        return Seq(x * 2)