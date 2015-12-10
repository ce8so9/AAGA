#!/usr/bin/env python3

import random
import pydot

graph = pydot.Dot(graph_type="digraph")

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def isLeaf(self):
        return self.left == None and self.right == None

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

def drawTree(root):

    if root == None or root.rootid == None:
        return
    else:
        if not root.isLeaf():
            print(root.rootid)
            if root.left:
                edge_left = pydot.Edge(str(root.rootid), str(root.left.key))
                graph.add_edge(edge_left)

            if root.right:
                edge_right = pydot.Edge(str(root.rootid), str(root.right.key))
                graph.add_edge(edge_right)

            printTree(root.left)
            printTree(root.right)

def remy(N):
    tree = BinaryTree(1)
    k = 1
    tab = [tree]

    while k < N + 1:

        hit = random.randint(0, 2*(k-1))
        curr = tab[hit]
        b = random.randint(0, 1)

        k = k + 1
        new_leaf = BinaryTree(k)
        new_int_node = BinaryTree(None)
        tab.append(new_leaf)
        tab.append(new_int_node)

        if b == 0:
            new_int_node.insertLeft(tree)
            new_int_node.insertRight(new_leaf)
        else:
            new_int_node.insertLeft(new_leaf)
            new_int_node.insertRight(tree)

        tab[k] = new_int_node

    print(len(tab))
    return tree

def main():
    # nbre de noeuds internes
    drawTree(remy(6))
    graph.write_png("remy.png")

if __name__ == "__main__":
    main()
