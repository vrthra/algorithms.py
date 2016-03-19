import doctest
from hypothesis import given
import hypothesis.strategies as st

def siftup(items, i):
  while i > 0:
      p = (i-1)//2
      if items[p] < items[i]:
         items[p], items[i] = items[i], items[p]
      i = p
  return items

def siftdown(items, last):
    p = 0
    while p <= last:
        l = 2 * p + 1
        r = l + 1
        max = p
        if l <= last and items[max] <= items[l]: max = l
        if r <= last and items[max] <= items[r]: max = r
        if max == p: break
        items[p], items[max] = items[max], items[p]
        p = max
    return items

def heapsort(items):
    """
    >>> heapsort([])
    []
    >>> heapsort([1])
    [1]
    >>> heapsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> heapsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    for i,t in enumerate(items):
        items = siftup(items, i)
    for i in reversed(range(len(items)-1)):
        items[i+1], items[0] = items[0], items[i+1]
        items = siftdown(items, i)
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
    assert heapsort(x) == sorted(x)

if __name__ == '__main__':
    test_sort()

