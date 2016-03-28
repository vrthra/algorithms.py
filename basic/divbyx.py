
import doctest
def divbyx(num, base):
    """
    >>> divbyx(0,2)
    [0]
    >>> divbyx(1,2)
    [1]
    >>> divbyx(2,2)
    [1, 0]
    >>> divbyx(3,2)
    [1, 1]
    >>> divbyx(6,4)
    [1, 2]
    """
    arr = []
    while num >= 0:
        i = num % base
        num = num // base
        arr.insert(0,i)
        if num == 0:
            break
    return arr

doctest.testmod(verbose=False)
