# Functor
def map(self, f):
    # type: (Callable[[A], B]) -> Seq[B]
    return Seq(*[f(x) for x in self])