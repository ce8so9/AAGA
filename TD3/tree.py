class AUB():

    def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

    def isLeaf(self):
        return self.left == None and self.right == None

    def isUnary(self):
        return (self.left != None or self.right != None) and not (self.left != None  and self.right != None)

    def isBinary(self):
        return self.left != None and self.right != None
