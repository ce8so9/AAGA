#!/usr/bin/env python3

import random
import argparse

import pydot
import math

# graph = pydot.Dot(graph_type="digraph")
graph = pydot.Dot(graph_type='digraph', nodesep=.75)
array_and_mat = None

class AUB():
    def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

    @staticmethod
    def printTree(root):
        if root == None:
            pass
        else:
            if root.left:
                edge_left = pydot.Edge(str(root.key), str(root.left.key))
                graph.add_edge(edge_left)

            if root.right:
                edge_right = pydot.Edge(str(root.key), str(root.right.key))
                graph.add_edge(edge_right)

            if not root.left and not root.right:
                graph.add_node(pydot.Node(root.key))

            AUB.printTree(root.left)
            AUB.printTree(root.right)

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

    global array_and_mat
    array_and_mat = pop(n)
    t = array_and_mat[0]
    comb_matrix = array_and_mat[1]
    nb_of_trees = t[len(t)-1]
    print("number of tree of height {0} : {1}".format(n, nb_of_trees))
    unary_tree_nb = t[len(t)-2]

    if tree_num == -1:
        hit = random.randint(1, nb_of_trees)
        # hit = 600
    else:
        hit = tree_num

    print("picking the {0}th tree".format(hit))
    print("if {0} <= {1} then unary".format(hit, unary_tree_nb))

    if hit <= unary_tree_nb:
        node.left = AUB(n-1)
        gen(n-1, node.left, hit)
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
        print(trace)

        print("k : {0}, n - k : {1}".format(found_k, found_nk))
        print(t)
        print(comb_matrix)
        print("stopped at {0} before S exceed {1}".format(trace[len(trace)-1], hit))

        tree_num = hit - trace[len(trace)-1]
        print("selected tree number config : {0}".format(tree_num))

        couples = [(i, j) for i in range(t[found_k-1]) for j in range(t[found_nk-1])]

        # print(couples)
        # print(len(couples))
        # print(couples[tree_num-1])

        tree_num_left = couples[tree_num-1][0]
        tree_num_right = couples[tree_num-1][1]

        node.left = AUB(n-1)
        node.right = AUB(n-2)

        gen(found_k, node.left, tree_num_left)
        gen(found_nk, node.right, tree_num_right)

def main():
    parser = argparse.ArgumentParser(description='AUB generator')
    parser.add_argument("N", help="number of nodes", type=int)

    args = parser.parse_args()
    global array_and_mat
    array_and_mat = pop(args.N)
    root = AUB(args.N)
    gen(args.N, root)
    AUB.printTree(root)
    global graph
    graph.add_node(pydot.Node('graph'))
    graph.write_png("gen_aub.png")

if __name__ == "__main__":
    main()

