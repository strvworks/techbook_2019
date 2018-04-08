from latex_lcg import lcg
from latex_lcg import RAND_MAX

gen = lcg()
i = 0
for i in range(0,2000):
    x = next(gen)/RAND_MAX
    y = next(gen)/RAND_MAX
    z = next(gen)/RAND_MAX
    print(f"{i}:({x},{y},{z})")
    with open("coodinates.dat","a") as f:
        f.write(f"{x} {y} {z}\n")
