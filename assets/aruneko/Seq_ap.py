# Applicative
def ap(self, fs):
    # type: (Seq[Callable[[A], B]]) -> Seq[B]
    return Seq(*[f(x) for f in fs for x in self])