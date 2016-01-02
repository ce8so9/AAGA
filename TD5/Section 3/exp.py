#!/usr/bin/env python3

import argparse
import random
from timer import Timer

def classicalpow(x, n):
    r = 1
    while n > 0:
        if n & 1:
            r = r * x
        n = n >> 1
        x = x * x
    return r

def unrolledpow(x, n):
    r = 1
    while n > 0:
        t = x * x
        if n & 1:
            r = r * x
        if n & 2:
            r = r * t
        n = n >> 2
        x = t * t
    return r

def guidedpow(x, n):
    r = 1
    while n > 0:
        t = x * x
        if n & 3:
            if n & 1:
                r = r * x
            if n & 2:
                r = r * t
        n = n >> 2
        x = t * t
    return r

def gen_times(fn, nb_its):

    res = []

    for i in range(nb_its):

        x = 0.5
        n = random.randint(0, 2**26 - 1)

        with Timer() as t:
            fn(x, n)
        res.append(t.msecs)

    return res


def main():

    parser = argparse.ArgumentParser(description='exponentiation by squaring performance')
    parser.add_argument("N", help="number of iterations", type=int)

    args = parser.parse_args()

    classical_times = gen_times(classicalpow, args.N)
    unrolled_times = gen_times(unrolledpow, args.N)
    guided_times = gen_times(guidedpow, args.N)

    import matplotlib.pyplot as plt

    plt.plot(range(1, args.N), classical_times)
    plt.plot(range(1, args.N), unrolled_times)
    plt.plot(range(1, args.N), guided_times)
    plt.show()

if __name__ == "__main__":
    main()
