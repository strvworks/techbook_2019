from latex_lcg import lcg
from latex_lcg import RAND_MAX
gen = lcg()
i = 0
first_gen = next(gen)
for i in range(0,RAND_MAX):
    x = next(gen)
    if x == first_gen:
        print(f"{i}:{x}")
