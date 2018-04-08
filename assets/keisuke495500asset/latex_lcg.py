RAND_MAX = 2147483647
def lcg(seed = 123456789):
    A = 127773
    B = 2836
    C = 16807
    s_n = seed
    while True:
        s_nn = -int(s_n/A)*B + C*(s_n % A)
        if s_nn < 0:
            s_nn += RAND_MAX
        yield s_nn
        s_n = s_nn
