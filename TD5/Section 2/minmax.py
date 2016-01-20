#!/usr/bin/env python3

import argparse
import random
from timer import Timer

def gen_array(size):
   return [random.random() for i in range(size)]

def naive_min_max(T):
    min = max = T[0]
    for i in range(1, len(T)):
        if (T[i] < min):
            min = T[i]
        if (T[i] > max):
            max = T[i]
    return (min, max)

def min_max_32(T):
    min = max = T[len(T)-1]
    for i in range(0, len(T)-1, 2):
        if (T[i] < T[i+1]):
            if (T[i] < min): min = T[i]
            if (T[i+1] > max): max = T[i+1]
        else:
            if (T[i+1] < min): min = T[i+1]
            if (T[i] > max): max = T[i]
    return (min, max)

def main():
    parser = argparse.ArgumentParser(description='minmax performance')
    parser.add_argument("N", help="test array max size", type=int)

    args = parser.parse_args()
    res = ()

    opt_times = []
    naive_times = []

    for i in range(1, args.N, 1000000):
        test = gen_array(i)

        with Timer() as t:
            res = naive_min_max(test)
        naive_times.append(t.secs)

        with Timer() as t:
            res = min_max_32(test)
        opt_times.append(t.secs)

    import matplotlib.pyplot as plt

    naive_plot = plt.plot(range(1, args.N, 1000000), naive_times, label="Naive mix & max")
    opt_plot = plt.plot(range(1, args.N, 1000000), opt_times, label="Optimized min & max")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel('array size')
    plt.ylabel('time (in sec)')
    plt.show()

if __name__ == "__main__":
    main()
