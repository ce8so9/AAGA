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

    res = 0
    x = float(2)

    for i in range(nb_its):
        n = random.randint(0, 2**26 - 1)

        with Timer() as t:
            fn(x, n)
        res = res + t.secs

    return res


def main():

    parser = argparse.ArgumentParser(description='exponentiation by squaring performance')
    parser.add_argument("N", help="number of iterations", type=int)

    args = parser.parse_args()

    classical_time = gen_times(classicalpow, args.N)
    unrolled_time = gen_times(unrolledpow, args.N)
    guided_time = gen_times(guidedpow, args.N)

    res = [classical_time, unrolled_time, guided_time]

    ind = range(3)
    width = 0.35

    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, res, width, color='red')

    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylabel('Execution time (en secs)')
    ax.set_title('exponentiation by squaring performance (50M computations)')

    xTickMarks = ['Classical', 'Unrolled', 'Guided']
    ax.set_xticks(list(map(lambda x : x + width, ind)))
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)

    plt.show()

if __name__ == "__main__":
    main()
