import doctest
from hypothesis import given
import hypothesis.strategies as st

def selectionsort(items):
    """
    >>> selectionsort([])
    []
    >>> selectionsort([1])
    [1]
    >>> selectionsort([1, 0])
    [0, 1]
    >>> selectionsort([2, 1, 0])
    [0, 1, 2]
    >>> selectionsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> selectionsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    for k in range(len(items)-1,0,-1):
        v,i = max((v,i) for i,v in enumerate(items[:k]))
        if items[k] < v:
            items[k],items[i] = items[i], items[k]
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert selectionsort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
