#!/usr/bin/env python3

import random
import argparse

import pydot
import math

graph = pydot.Dot(graph_type="digraph")
i = 0

# takes an array and return sigma(k<-[1..n])A(k)A(n-k)
def comb(t, n, combs):
    assert n <= len(t) and len(t) > 0
    k = 0
    nk = n - 1
    # assert nk >= 0
    res = 0
    while k < n:
        # print("A{0}A{1} eq {2}".format(k+1, nk+1, t[k]*t[nk]))
        res = res + t[k]*t[nk]
        combs[k][nk] = t[k]*t[nk]
        nk = nk - 1
        k = k + 1

    return res

def pop(n):
    t = [1]
    c = [[-1 for x in range(n)] for y in range(n)]
    for i in range(1, n):
        term = t[i-1] + comb(t, i-1, c)
        t.append(term)
        # print("A{0}({1}) = A{2}({3}) + ".format(i, term, i-1, t[i-1]))
        # print("--------------------")
    # print(t)
    # assert list(t[0::4]) == [1, 1, 2, 4, 9]
    return (t, c)

def gen(n):
    array_and_mat = pop(n)
    t = array_and_mat[0]
    comb_matrix = array_and_mat[1]
    maxint = t[len(t)-1]
    un = t[len(t)-2]

    # hit = random.randint(1, maxint)
    hit = 600
    hum = [un]
    if hit <= un:
        print("unary")
        # gen a unary tree of size n - 1
    else:
        i = 0
        j = len(t)-3
        S = un
        while S <= 600 and i < len(t)-3:
            S = S + comb_matrix[i][j]
            hum.append(comb_matrix[i][j])
            i = i + 1
            j = j - 1
            print(S)
        found_k = i - 1
        found_nk = n - found_k - 1
        print("k : {0}, n - k : {1}".format(found_k, found_nk))
        print(S - comb_matrix[i-1][j+1])
        tree_num = hit - (S - comb_matrix[i-1][j+1])
        print(tree_num)
        couples = [(i, j) for i in range(t[found_nk-1]) for j in range(t[found_k-1])]
        print(couples)
        print(len(couples))
        print(couples[tree_num-1])


def main():
    parser = argparse.ArgumentParser(description='AUB generator')
    parser.add_argument("N", help="number of nodes", type=int)

    args = parser.parse_args()
    gen(args.N)

if __name__ == "__main__":
    main()

