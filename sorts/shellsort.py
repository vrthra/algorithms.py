import doctest
from hypothesis import given
import hypothesis.strategies as st

def shellsort(items):
    """
    >>> shellsort([])
    []
    >>> shellsort([1])
    [1]
    >>> shellsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> shellsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    def sort_gap(start, gap):
        for k in range(len(items)-1, 0, -1*gap):
            v,i = max((v,i) for i,v in enumerate(items[:k:gap]))
            if items[k] < v:
                items[k], items[i] = items[i], items[k]

    gap = len(items)//2
    while gap > 0:
        for i in range(gap):
            sort_gap(i, gap)
        gap = gap//2
    return items

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert shellsort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
