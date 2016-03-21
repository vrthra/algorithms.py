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
    self._data = [data, None, None]


  def __repr__(self): return str(self._data)


  @property
  def data(self): return self._data[0]


  @property
  def left(self): return self._data[1]


  @property
  def right(self): return self._data[2]


  @data.setter
  def data(self, new):
    self._data[0] = new
    return self


  @left.setter
  def left(self, new):
    self._data[1] = new
    return self


  @right.setter
  def right(self, new):
    self._data[2] = new
    return self

if __name__ == '__main__':
  doctest.testmod()


