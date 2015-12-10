#!/usr/bin/env python3

import random
import argparse

import pydot
import math

graph = pydot.Dot(graph_type="digraph")
i = 0

class AUB():

    def __init__(self, key):
      self.left = None
      self.right = None
      self.parent = None
      self.key = key

    def isLeaf(self):
        return self.left == None and self.right == None

    def isUnary(self):
        return (self.left != None or self.right != None) and not (self.left != None  and self.right != None)

    def isBinary(self):
        return self.left != None and self.right != None

    @staticmethod
    def printTree(root):
        global i

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

def head_or_tails():
    return random.randint(0, 2)

def aub_gen(N):
    k = 1
    tree = AUB(1)
    nodes = [tree]
    weighted_nodes = []

    while k < N :

        for node in nodes:
            if node.isLeaf():
                for i in range(3):
                    weighted_nodes.append(node)
            elif node.isUnary():
                for i in range(2):
                    weighted_nodes.append(node)
            else:
                weighted_nodes.append(node)

        hit = random.randint(0, len(weighted_nodes) - 1)
        curr = weighted_nodes[hit]
        weighted_nodes = []

        ht_res1 = head_or_tails()
        ht_res2 = head_or_tails()
        new_leaf = AUB(k+1)

        if curr.isLeaf():
            print("{0} est une feuille".format(curr.key))
            print(curr.__dict__)
            if ht_res1:
                if ht_res2:
                    curr.left = new_leaf
                else:
                    curr.right = new_leaf
            else:
                if curr.parent == None:
                    curr.parent = new_leaf

                parent = curr.parent

                if ht_res2:
                    new_leaf.left = curr
                else:
                    new_leaf.right = curr

                if parent.left == curr:
                    parent.left = new_leaf

                if parent.right == curr:
                    parent.right = new_leaf

        elif curr.isUnary():
            print("{0} est noeud unaire".format(curr.key))
            print(curr.__dict__)
            if ht_res1:
                if curr.left:
                    curr.right = new_leaf
                else:
                    curr.left = new_leaf
            else:
                if curr.parent == None:
                    curr.parent = new_leaf

                parent = curr.parent

                if ht_res2:
                    new_leaf.left = curr
                else:
                    new_leaf.right = curr

                if parent.left == curr:
                    parent.left = new_leaf

                if parent.right == curr:
                    parent.right = new_leaf
        else:
            print("{0} est noeud binaire".format(curr.key))
            print(curr.__dict__)
            if curr.parent == None:
                curr.parent = new_leaf

            parent = curr.parent

            if ht_res2:
                new_leaf.left = curr
            else:
                new_leaf.right = curr

            if parent.left == curr:
                parent.left = new_leaf

            if parent.right == curr:
                parent.right = new_leaf

        nodes.append(new_leaf)
        k = k + 1

    print(len(nodes))
    # for n in nodes:
        # if n.isBinary()

    return tree

def main():
    parser = argparse.ArgumentParser(description='AUB generator')
    parser.add_argument("N", help="number of internal nodes", type=int)

    args = parser.parse_args()

    t = aub_gen(args.N)
    AUB.printTree(t)
    graph.write_png("gen_aub.png")

if __name__ == "__main__":
    main()
