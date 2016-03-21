import doctest

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def mytest():
  """
  >>> r = BinaryTree(3)
  >>> insertLeft(r,4)
  [3, [4, [], []], []]
  >>> insertLeft(r,5)
  [3, [5, [4, [], []], []], []]
  >>> insertRight(r,6)
  [3, [5, [4, [], []], []], [6, [], []]]
  >>> insertRight(r,7)
  [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
  >>> l = getLeftChild(r)
  >>> l
  [5, [4, [], []], []]
  >>> setRootVal(l,9)
  >>> r
  [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
  >>> insertLeft(l,11)
  [9, [11, [4, [], []], []], []]
  >>> r
  [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
  >>> getRightChild(getRightChild(r))
  [6, [], []]
  """
  pass


if __name__ == '__main__':
    doctest.testmod()
