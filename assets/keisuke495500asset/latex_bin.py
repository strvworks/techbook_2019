from latex_lcg import lcg
from latex_lcg import RAND_MAX

# True: A
# False: B
def binarize_rnd(random_number):
    return random_number < 0.5

def count_K(rnd_bins):
    K = 0
    for i in range(1, len(rnd_bins)):
        if not rnd_bins[i-1] == rnd_bins[i]:
            K += 1
    return K+1

gen = lcg()
n = 200000
rnd_bins = [binarize_rnd(next(gen)/RAND_MAX) for x in range(0,n)]
print(f"A:{rnd_bins.count(True)}")
print(f"B:{rnd_bins.count(False)}")
print(f"K:{count_K(rnd_bins)}")
