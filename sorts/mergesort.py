import doctest
from hypothesis import given
import hypothesis.strategies as st

def mergesort(items):
    """
    >>> mergesort([])
    []
    >>> mergesort([1])
    [1]
    >>> mergesort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> mergesort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    def merge(left, right):
        """
        >>> merge([2,4,6], [])
        [2, 4, 6]
        >>> merge([], [2,4,6])
        [2, 4, 6]
        >>> merge([1,3,6], [2,4,6])
        [1, 2, 3, 4, 6, 6]
        """
        if not left: return right
        elif not right: return left
        elif left[0] < right[0]:
            return left[:1] + merge(left[1:], right)
        else:
            return right[:1] + merge(left, right[1:])
    if len(items) <= 1 : return items
    mid = len(items)//2
    left = mergesort(items[:mid])
    right = mergesort(items[mid:])
    return merge(left, right)

@given(st.lists(elements=st.integers()))
def test_sort(x):
      assert mergesort(x) == sorted(x)

if __name__ == '__main__':
  test_sort()
