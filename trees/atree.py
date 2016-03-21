import doctest

class BTree:
  """
  >>> n = BTree(1)
  >>> n
  [1, None, None]
  >>> n.left = BTree(2)
  >>> n.right = BTree(3)
  >>> n
  [1, [2, None, None], [3, None, None]]
  >>> x = BTree('a')
  >>> x
  ['a', None, None]
  >>> x.left = BTree('b')
  >>> x
  ['a', ['b', None, None], None]
  >>> x.right = BTree('c')
  >>> x
  ['a', ['b', None, None], ['c', None, None]]
  >>> x.right.right = BTree('d')
  >>> x
  ['a', ['b', None, None], ['c', None, ['d', None, None]]]
  >>> x.right.right.left = BTree('e')
  >>> x
  ['a', ['b', None, None], ['c', None, ['d', ['e', None, None], None]]]
  """

  def __init__(self, data):
    self._data = data
    self._left = None
    self._right = None


  def __repr__(self): return str([self._data, self._left, self._right])


  @property
  def data(self): return self._data


  @property
  def left(self): return self._left


  @property
  def right(self): return self._right


  @data.setter
  def data(self, new):
    self._data = new
    return self


  @left.setter
  def left(self, new):
    self._left = new
    return self


  @right.setter
  def right(self, new):
    self._right = new
    return self

if __name__ == '__main__':
  doctest.testmod()


