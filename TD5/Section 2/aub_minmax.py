#!/usr/bin/env python3

import random
import argparse
import math
from timer import Timer

class AUB():
    def __init__(self):
      self.left = None
      self.right = None
      self.number = -1

    @staticmethod
    def height(node):
        if node is None:
            return 0
        else:
            return max(AUB.height(node.left), AUB.height(node.right)) + 1

    @staticmethod
    def size(root, count = 0):
        if root is None:
            return count
        return AUB.size(root.left, AUB.size(root.right, count + 1))

# takes an array and return sigma(k<-[1..n])A(k)A(n-k)
def comb(t, n, combs):
    assert n <= len(t) and len(t) > 0
    k = 0
    nk = n - 1
    res = 0

    while k < n:
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
    return (t, c)

def gen(n, node, tree_num=-1):

    if n <= 1 or node == None:
        return

    t, comb_matrix = pop(n)
    nb_of_trees = t[len(t)-1]
    unary_tree_nb = t[len(t)-2]

    if tree_num == -1:
        hit = random.randint(1, nb_of_trees)
    else:
        hit = tree_num

    node.number = hit

    if hit <= unary_tree_nb:
        node.left = AUB()
        gen(n-1, node.left, hit)
        return node
    else:
        i = 0
        j = len(t)-3
        S = unary_tree_nb
        trace = [unary_tree_nb]
        while S <= hit and i <= len(t)-3:
            S = S + comb_matrix[i][j]
            if S <= hit:
                trace.append(S)
            i = i + 1
            j = j - 1

        found_k = i
        found_nk = n - found_k - 1
        assert(n == found_k + found_nk + 1)

        tree_num = hit - trace[len(trace)-1]

        couples = [(i, j) for i in range(t[found_k-1]) for j in range(t[found_nk-1])]

        tree_num_left = couples[tree_num-1][0]
        tree_num_right = couples[tree_num-1][1]

        node.left = AUB()
        node.right = AUB()

        gen(found_k, node.left, tree_num_left)
        gen(found_nk, node.right, tree_num_right)

        return node

def gen_tree_array(array_size, tree_size):
   return [gen(tree_size, AUB()) for i in range(array_size)]

def naive_min_max(T):
    min = max = T[0].number
    for i in range(1, len(T)):
        if (T[i].number < min):
            min = T[i].number
        if (T[i].number > max):
            max = T[i].number
    return (min, max)

def min_max_32(T):
    min = max = T[len(T)-1].number
    for i in range(0, len(T)-1, 2):
        if (T[i].number < T[i+1].number):
            if (T[i].number < min): min = T[i].number
            if (T[i+1].number > max): max = T[i+1].number
        else:
            if (T[i+1].number < min): min = T[i+1].number
            if (T[i].number > max): max = T[i].number
    return (min, max)

def main():
    parser = argparse.ArgumentParser(description='AUB minmax performance')
    parser.add_argument("N", help="maximum array size", type=int)
    parser.add_argument("S", help="size of generated trees", type=int)

    args = parser.parse_args()
    res = ()

    opt_times = []
    naive_times = []

    for i in range(1, args.N, 10000):
        test = gen_tree_array(i, args.S)

        with Timer() as t:
            res = naive_min_max(test)
        naive_times.append(t.secs)

        with Timer() as t:
            res = min_max_32(test)
        opt_times.append(t.secs)

    import matplotlib.pyplot as plt

    naive_plot = plt.plot(range(1, args.N, 10000), naive_times, label="Naive mix & max")
    opt_plot = plt.plot(range(1, args.N, 10000), opt_times, label="Optimized min & max")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel('array size')
    plt.ylabel('time (in sec)')
    plt.suptitle('Minmax performance on unary-binary tree of size ' + str(args.S), fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()

