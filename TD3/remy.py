#!/usr/bin/env python3

import random

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

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

def printTree(tree):
        if tree != None:
            print(tree.getNodeValue())
            printTree(tree.getLeftChild())
            printTree(tree.getRightChild())
        else:
            print("()")

def remy(N):
    tree = BinaryTree(0)
    k = 0
    tab = [tree]

    while k < N:

        hit = random.randint(0, 2*k)
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
    printTree(remy(6))

if __name__ == "__main__":
    main()
