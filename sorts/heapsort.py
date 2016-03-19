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
    """
    >>> siftdown([1, 0, 1],2)
    [1, 0, 1]
    > >> siftdown([0, 0], 1)
    [0, 0]
    > >> siftdown([0, 1, 0, 1], 3)
    [1, 1, 0, 0]
    > >> siftdown([0, 2, 0, 1, 0, 0], 5)
    [2, 1, 0, 0, 0, 0]
    >>> siftdown([0,1,0,1,0,0,1, 0,0,0,0], 10)
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    """
    p = 0
    while p <= last:
        #print(items)
        l = 2 * p + 1
        r = l + 1
        #print(items,p,l,r)
        max = p
        if l <= last and items[max] <= items[l]:
            max = l
        if r <= last and items[max] <= items[r]:
            max = r
        #print(max)
        if max != p:
            items[p], items[max] = items[max], items[p]
            p = max
        else:
            break
    return items

def isheap(A, size=-1):
    if size == -1: size = len(A)
    if size <= 1: return True
    return all(A[i] <= A[(i - 1) // 2] for i in range(1, size))

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
    >>> heapsort([1, 0, 1, 1, 0, 0])
    [0, 0, 0, 1, 1, 1]
    >>> heapsort([0, 0, 0, 0, 1, 2, 2])
    [0, 0, 0, 0, 1, 2, 2]

    >>> heapsort([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> heapsort([0, 1, 1, 1, 0, 0, 1, 0, 0, 0])
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    """
    for i,t in enumerate(items):
        #print('<',items[:i+1])
        items = siftup(items, i)
        #print('>',items[:i+1])
        #print(isheap(items,i+1), i)
        #print()
    if not isheap(items, len(items)): raise ValueError('not a heap %s' % str(items))
    for i in reversed(range(len(items)-1)):
        if not isheap(items, i+2):  raise ValueError('not a heap: %s %i' % (str(items), i))
        items[i+1], items[0] = items[0], items[i+1] # extract top and place the last one there.
        items = siftdown(items, i)
        if not isheap(items, i+1): raise ValueError('not a heap %s %i' % (str(items), i+1))
    return items


def mark(A):
    print(A)
    B = []
    A[0] = 0
    for i in range(1, len(A)): A[i] = (i - 1) // 2
    print(A)
    for i in range(0, len(A)): B.append(i)
    print(B)

@given(st.lists(elements=st.integers()))
def test_sort(x):
    assert heapsort(x) == sorted(x)


@given(st.lists(elements=st.integers()))
def test_siftdown(x):
    assert isheap(siftdown(x, len(x)-1), len(x)) == True

if __name__ == '__main__':
    test_sort()
    #doctest.testmod(verbose=False)

