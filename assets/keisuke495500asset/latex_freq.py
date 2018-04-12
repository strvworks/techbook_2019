from latex_lcg import lcg,RAND_MAX
from collections import defaultdict

def classifier(random_number):
    for i,x in zip(range(1,11), \
                 ["A","B","C","D","E","F","G","H","I","J"]):
        if random_number <= i*0.1:
            return x

gen = lcg()
n = 200000
chi = 0
real_freqs = defaultdict(lambda: 0)
for i in range(0,n):
    real_freqs[classifier(next(gen)/RAND_MAX)] += 1

for i,x in real_freqs.items():
    chi += (x - 20000)*(x - 20000)/20000
    print(f"{i}:{x}")
print(f"chi = {chi}")
