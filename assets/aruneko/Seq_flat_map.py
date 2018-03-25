# Monad
def flat_map(self, f):
    # type: (Callable[[A], Seq[B]]) -> Seq[B]
    return Seq(*[y for x in self for y in f(x)])