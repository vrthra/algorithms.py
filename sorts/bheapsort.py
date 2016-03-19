import doctest
from hypothesis import given
import hypothesis.strategies as st

def parent(i): return (i - 1)//2
def lchild(p): return 2 * p + 1
def rchild(p): return 2 * (p + 1)

def siftdown(items, start, last):
    p = start
    while p <= last:
        l = lchild(p)
        r = rchild(p)
        max = p
        if l <= last and items[max] <= items[l]: max = l
        if r <= last and items[max] <= items[r]: max = r
        if max == p: break
        items[p], items[max] = items[max], items[p]
        p = max
    return items

def bheapsort(items):
    """
    >>> bheapsort([])
    []
    >>> bheapsort([1])
    [1]
    >>> bheapsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> bheapsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    last = len(items) - 1
    start = parent(last)
    for start in reversed(range(0,start+1)):
        items = siftdown(items, start, len(items)-1)
    for i in reversed(range(len(items)-1)):
        items[i+1], items[0] = items[0], items[i+1]
        items = siftdown(items, 0, i)
    return items

@given(st.lists(elements=st.integers()))
def test_bheapsort(x):
    assert bheapsort(x) == sorted(x)

if __name__ == '__main__':
    test_bheapsort()
    doctest.testmod()

