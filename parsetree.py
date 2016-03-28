import doctest
import operator
from trees.atree import BTree
# If the current token is a '(', add a new node as the left child of the
# current node, and descend to the left child.
# If the current token is in the list ['+','-','/','*'], set the root value of
# the current node to the operator represented by the current token. Add a new
# node as the right child of the current node and descend to the right child.
# If the current token is a number, set the root value of the current node to
# the number and return to the parent.
# If the current token is a ')', go to the parent of the current node.

def buildParseTree(fpexp):
    """
    >>> v = buildParseTree("1")
    >>> v
    [1, None, None]
    >>> evaluate(v)
    1
    >>> v = buildParseTree("( 1 )")
    >>> v
    ['', [1, None, None], None]
    >>> evaluate(v)
    1
    >>> evaluate(buildParseTree("( 1 + 2 )"))
    3
    >>> buildParseTree("1 + 2")
    """

    fplist = fpexp.split()
    pStack = []
    eTree = BTree('')
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.left = BTree('')
            pStack.append(currentTree)
            currentTree = currentTree.left
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.data = int(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.data = i
            currentTree.right = BTree('')
            pStack.append(currentTree)
            currentTree = currentTree.right
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def parseTree(string):
  """
  >>> v = parseTree("1")
  >>> v
  ['1', None, None]
  >>> evaluate(v)
  1
  >>> v = parseTree("( 1 )")
  >>> v
  ['', ['1', None, None], None]
  >>> evaluate(v)
  1
  >>> evaluate(parseTree("( 1 + 2 )"))
  3
  >>> parseTree("1 + 2")
  """
  lst = string.split(' ')
  parent = []
  current = BTree('') 
  head = current
  parent.append(current)
  for token in lst:
     #print(token)
     if token == '(':
         current.left = BTree('')
         parent.append(current)
         current = current.left
     elif token == ')':
         current = parent.pop()
     elif token in ['+', '-', '*', '/']:
         current.data = token
         current.right = BTree('')
         parent.append(current)
         current = current.right
     else: # var
         current.data = token
         current = parent.pop()
  return head

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.left
    rightC = parseTree.right

    if leftC and rightC:
        fn = opers[parseTree.data]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.data

def evaluate1(tree):
    # post order
    if not tree: return None
    if tree.left == None and tree.right == None: return int(tree.data)
    l = evaluate(tree.left)
    r = evaluate(tree.right)
    o = tree.data
    if o == '' : return l
    if o == '+': return l + r
    if o == '-': return l - r
    if o == '*': return l * r
    if o == '/': return l / r
    return [tree.data, l, r]


# parseTree('( a * ( b + c ) + d )')
# parseTree('( a * ( b + c ) + d )')
doctest.testmod()
