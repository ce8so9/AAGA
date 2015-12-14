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

    for i in range(1, args.N):
        test = gen_array(i)

        with Timer() as t:
            res = naive_min_max(test)
        # print("=> naive : {0} ms".format(t.msecs))
        naive_times.append(t.msecs)

        with Timer() as t:
            res = min_max_32(test)
        # print("=> optimized : {0} ms".format(t.msecs))
        opt_times.append(t.msecs)

    import matplotlib.pyplot as plt

    # fig1, ax1 = plt.subplots()
    # fig2, ax2 = plt.subplots()
    plt.plot(range(1, args.N), naive_times)
    plt.plot(range(1, args.N), opt_times)
    plt.show()

if __name__ == "__main__":
    main()
