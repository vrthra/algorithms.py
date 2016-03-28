import doctest

def lsearch(item, arr):
    """
    >>> lsearch(1, [])
    >>> lsearch(1,[2])
    >>> lsearch(1,[1])
    0
    >>> lsearch(4,[1,2,3,4])
    3
    """
    pos = 0
    found = 0
    while pos < len(arr):
        if arr[pos] == item:
            return pos
        pos += 1
    return None


def bsearch(item, arr):
    """
    >>> bsearch(1, [])
    >>> bsearch(1,[2])
    >>> bsearch(1,[1])
    0
    >>> bsearch(4,[1,2,3,4,5])
    3
    >>> bsearch(4,[1,2,3,5])
    """
    def recurse(first, last):
        mid = (first + last)//2
        if (first > last): return None
        elif arr[mid] > item:
            return recurse(first, mid-1)
        elif arr[mid] < item:
            return recurse(mid+1, last)
        else:
            return mid
    return recurse(0,len(arr)-1)


def bsearch_i(item, arr):
    """
    >>> bsearch_i(1, [])
    >>> bsearch_i(1,[2])
    >>> bsearch_i(1,[1])
    0
    >>> bsearch_i(4,[1,2,3,4,5])
    3
    >>> bsearch_i(4,[1,2,3,5])
    """
    first = 0
    last = len(arr) -1
    while first <= last:
        mid = (first + last)//2
        if item < arr[mid]:
            last = mid - 1
        elif item > arr[mid]:
            first = mid + 1
        else:
            if arr[mid] == item:
                return mid
            else:
                return None
    return None

doctest.testmod()
