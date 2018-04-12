from latex_lcg import lcg
from latex_lcg import RAND_MAX
from collections import defaultdict

# <= 0.1 : A
# <= 0.2 : B
# <= 0.3 : C
# <= 0.4 : D
# <= 0.5 : E
# <= 0.6 : F
# <= 0.7 : G
# <= 0.8 : H
# <= 0.9 : I
# <= 1.0 : J
def classifier(random_number):
    if random_number <= 0.1:
        return "A"
    elif random_number <= 0.2:
        return "B"
    elif random_number <= 0.3:
        return "C"
    elif random_number <= 0.4:
        return "D"
    elif random_number <= 0.5:
        return "E"
    elif random_number <= 0.6:
        return "F"
    elif random_number <= 0.7:
        return "G"
    elif random_number <= 0.8:
        return "H"
    elif random_number <= 0.9:
        return "I"
    else:
        return "J"

gen = lcg()
n = 200000
real_freqs = defaultdict(lambda: 0)
for i in range(0,n):
    real_freqs[classifier(next(gen)/RAND_MAX)] += 1
for i,x in real_freqs.items():
    print(f"{i}:{x}")
