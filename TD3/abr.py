#!/usr/bin/env python3

import random
import argparse

import pydot
import math

graph = pydot.Dot(graph_type="digraph")
i = 0

class ABR():

    def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

    def isLeaf(self):
        return self.left == None and self.right == None

    def insert(self, newNode):
        if self.isLeaf():
            self.key = newNode.key
            self.left = newNode.left
            self.right = newNode.right

        if self.key < newNode.key:
            self.left.insert(newNode)
        else:
            self.right.insert(newNode)

    @staticmethod
    def printTree(root):
        global i 

        if root == None:
            pass
        else:
            if not root.isLeaf():

                if root.left.key != -1:
                    edge_left = pydot.Edge(str(root.key), str(root.left.key))

                if root.right.key != -1:
                    edge_right = pydot.Edge(str(root.key), str(root.right.key))

                if root.left.key == -1:
                    edge_left = pydot.Edge(str(root.key), "F%d" % i)
                    i = i + 1

                if root.right.key == -1:
                    edge_right = pydot.Edge(str(root.key), "F%d" % i)
                    i = i + 1

                graph.add_edge(edge_left)
                graph.add_edge(edge_right)
                ABR.printTree(root.left)
                ABR.printTree(root.right)

    @staticmethod
    def countIntNodes(root):
        if root == None or root.isLeaf():
            return 0
        else:
            return 1 + ABR.countIntNodes(root.left) + ABR.countIntNodes(root.right)

    @staticmethod
    def average_leaf_depth(root, lvl):
        if root == None or root.isLeaf():
            return (lvl, 1)
        else:
            lchild_depth = ABR.average_leaf_depth(root.left, lvl+1);
            rchild_depth = ABR.average_leaf_depth(root.right, lvl+1);

            return (lchild_depth[0] + rchild_depth[0], lchild_depth[1] + rchild_depth[1])

def abr_gen(N):
    tree = ABR(-1)
    k = 0
    leafs = [tree]

    while k < N:

        hit = random.randint(0, k)
        curr = leafs[hit]

        new_int_node = ABR(-1)
        new_int_node.left = ABR(-1)
        new_int_node.right = ABR(-1)

        curr.left = ABR(-1)
        curr.right = ABR(-1)

        leafs.append(curr.left)
        leafs.append(curr.right)

        leafs.remove(curr)

        k = k + 1

    return tree

def abr_label(tab, root):
    if tab == [] or root == None:
        return    
    else:
        nb_g_int_nodes = ABR.countIntNodes(root.left)
        nb_d_int_nodes = ABR.countIntNodes(root.right)
        select = -1

        if nb_g_int_nodes < nb_d_int_nodes:
            select = tab[nb_d_int_nodes]
            abr_label(tab[0:nb_d_int_nodes], root.right)
            abr_label(tab[nb_d_int_nodes+1:], root.left)
        else:
            select = tab[nb_g_int_nodes]
            abr_label(tab[0:nb_g_int_nodes], root.left)
            abr_label(tab[nb_g_int_nodes+1:], root.right)

        root.key = select

def mean_depth(length, tree_nb):
    curr_depth = None
    depth_arr = []
    for i in range(tree_nb):
        curr_depth = ABR.average_leaf_depth(abr_gen(length), 0)
        depth_arr.append(curr_depth[0])
    
    return sum(depth_arr) / (tree_nb * curr_depth[1])

def main():
    parser = argparse.ArgumentParser(description='ABR generator')
    parser.add_argument("N", help="number of internal nodes", type=int)
    parser.add_argument("-m", help="generate graph for average depth of trees - number of trees to generate", type=int)

    args = parser.parse_args()
    
    if args.m:
        size = args.N
        average_depths = [mean_depth(i, args.m) for i in range(size)]

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot(range(size), average_depths)
        print( "constant : " + str(average_depths[size - 1] / math.log(size)) )
        plt.show()
    else:
        t = abr_gen(args.N)
        abr_label(list(range(1, args.N + 1)), t)
        ABR.printTree(t)
        print(ABR.depth(t, 0))
        graph.write_png("gen_abr.png")

if __name__ == "__main__":
    main()
