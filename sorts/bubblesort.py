import doctest
from hypothesis import given
import hypothesis.strategies as st

def bubblesort(items):
    """
    >>> bubblesort([])
    []
    >>> bubblesort([1])
    [1]
    >>> bubblesort([1, 0])
    [0, 1]
    >>> bubblesort([2, 1, 0])
    [0, 1, 2]
    >>> bubblesort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> bubblesort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    for i in range(len(items)):
        mod = False
        for j in range(len(items)-1):
            if items[j+1] < items[j]:
                mod = True
                items[j+1], items[j] = items[j], items[j+1]
        if not mod: break
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert bubblesort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
