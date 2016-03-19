import doctest
from hypothesis import given
import hypothesis.strategies as st

def partition(items, begin, end, pivot):
    f = begin + 1
    l = end
    while True:
        while f <= l and items[f] <= pivot: f+=1
        while f <= l and items[l] >= pivot: l-=1
        if f < l: items[l], items[f] = items[f], items[l]
        else: break
    items[l], items[begin] = items[begin], items[l]
    return l

def qsort(items, fst, lst):
    if fst >= lst: return
    pivot = items[fst]
    l = partition(items, fst, lst, pivot)
    qsort(items, fst, l-1)
    qsort(items, l+1, lst)

def quicksort(items):
    """
    >>> quicksort([])
    []
    >>> quicksort([1])
    [1]
    >>> quicksort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> quicksort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    >>> quicksort([0, 0, 0, 1, 0, 0, 0])
    [0, 0, 0, 0, 0, 0, 1]
    """
    if not items: return items
    qsort(items, 0, len(items)-1)
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert quicksort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
  # doctest.testmod()
