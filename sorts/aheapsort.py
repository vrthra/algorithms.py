import doctest
from hypothesis import given, note
import hypothesis.strategies as st

def parent(i): return (i - 1) // 2


def lchild(p): return 2 * p + 1


def rchild(p): return 2 * (p + 1)


def findleaf(item, i, last):
    """
    Find the maximum child path, and return the index of that child.
    """
    while i <= last:
        l = lchild(i)
        r = rchild(i)
        if r > last:
            if l <= last:
                i = l
            break
        elif item[l] > item[r]:
            i = l
        else:
            i = r
    return i


def siftdown(items, i, last):
    j = findleaf(items, i, last)

    # we have the maximum path child in j. Now, find where
    # we (i) are in this path. `j` will contain our parent
    while items[i] > items[j]: j = parent(j)

    # save current parent `j` on x
    # put [i] on [j]
    x, items[j] = items[j], items[i]
    
    # swap x up the tree.
    while j > i:
        j = parent(j)
        x, items[j] = items[j], x
    return items


def aheapsort(items):
    """
    >>> aheapsort([])
    []
    >>> aheapsort([1])
    [1]
    >>> aheapsort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> aheapsort([4,5,3,1,2])
    [1, 2, 3, 4, 5]
    """
    if len(items) <= 1: return items

    last = len(items) - 1
    start = parent(last)
    for start in reversed(range(0, start + 1)):
        items = siftdown(items, start, len(items) - 1)

    for i in reversed(range(len(items) - 1)):
        items[i + 1], items[0] = items[0], items[i + 1]
        items = siftdown(items, 0, i)
    return items


@given(st.lists(elements=st.integers()))
def test_bheapsort(x):
    assert aheapsort(x) == sorted(x)


if __name__ == '__main__':
    test_bheapsort()
    doctest.testmod()
