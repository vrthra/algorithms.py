import doctest
from hypothesis import given
import hypothesis.strategies as st

def find_the_place(items, v, till):
    """
    >>> items = [1,2,4]
    >>> find_the_place(items, 3, 3)
    2
    """
    for i,val in enumerate(items[:till]):
        if v < val: return i
    return till

def insertionsort(items):
    """
    >>> insertionsort([])
    []
    >>> insertionsort([1])
    [1]
    >>> insertionsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> insertionsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]

    """
    for k in range(1,len(items)):
        i = find_the_place(items, items[k], k)
        items[i], items[i+1:k+1] = items[k], items[i:k]
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert insertionsort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
