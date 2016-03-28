
import doctest
class IStack:
    def push(self,item):
        pass
    def pop(self):
        pass
    def isEmpty(self):
        pass
    
class LStack(IStack):
    """
    >>> s = LStack(4)
    >>> s.isEmpty()
    True
    >>> s.push(1)
    >>> s.isEmpty()
    False
    >>> s.pop()
    1
    >>> s.pop()
    Traceback (most recent call last):
    ...
    ValueError: Elements < 4
    """
    def __init__(self, elts=100):
        self._elts = elts
        self._arr = [None] * self._elts
        self._current=-1
    def push(self, item):
        if self._current == self._elts: raise ValueError('Elements > %s' % self._elts)
        self._current += 1
        self._arr[self._current] = item
    def pop(self):
        if self._current < 0: raise ValueError('Elements < %s' % self._elts)
        v = self._arr[self._current]
        self._current-=1
        return v
    def isEmpty(self):
        return self._current == -1

class SStack(IStack):
    """
    >>> s = SStack()
    >>> s.isEmpty()
    True
    >>> s.push(1)
    >>> s.isEmpty()
    False
    >>> s.pop()
    1
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: pop from empty list
    """
    def __init__(self):
        self._arr = []
    def push(self,i):
        self._arr.insert(0,i)
    def pop(self):
        return self._arr.pop(0)
    def isEmpty(self):
        return len(self._arr) == 0

def parCheck(items):
    """
    >>> parCheck('')
    True
    >>> parCheck('(')
    False
    >>> parCheck(')')
    False
    >>> parCheck('()()')
    True
    """
    s = SStack()
    x = {'(':')','{':'}','<':'>'}
    for i in items:
        if i in ['(','<','{']:
            s.push(i)
        elif i in [')','>','}']:
            if s.isEmpty():
                return False
            v = s.pop()
            if x[v] != i:
                return False
    return s.isEmpty()
                   
doctest.testmod()
