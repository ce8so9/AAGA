#!/usr/bin/env python3

import argparse

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
    parser = argparse.ArgumentParser(description='AUB generator')
    parser.add_argument("N", help="number of nodes", type=int)

    args = parser.parse_args()
    test = [9, 4, 3, 2, 1, 5, 8]
    res = naive_min_max(test)
    print("min : {0}, max : {1}".format(res[0], res[1]))
    res = min_max_32(test)
    print("min : {0}, max : {1}".format(res[0], res[1]))

if __name__ == "__main__":
    main()
