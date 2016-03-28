
import doctest

class IHash:
    def __init__(self):
        pass
    def hashit(self, i):
        pass
    def get(self, i):
        pass
    def put(self, i):
        pass   
class OHash(IHash):
    """
    >>> h = OHash(4)
    >>> h.put(1,10)
    [None, (1, 10), None, None]
    >>> h.put(1,11)
    [None, (1, 11), None, None]
    >>> h.put(2,20)
    [None, (1, 11), (2, 20), None]
    >>> h.put(0,0)
    [(0, 0), (1, 11), (2, 20), None]
    >>> h.put(4,30)
    [(0, 0), (1, 11), (2, 20), (4, 30)]
    >>> h.get(2)
    20
    >>> h.get(4)
    30
    """
    def __init__(self, n):
        self._arr = [None] * n
        self._n = n
    def __repr__(self):
        return str(self._arr)
    
    def hashit(self, i):
        return i % self._n
        
    def put(self, k, v):
        t = self.hashit(k)
        while t < self._n:
            if not self._arr[t]:
                self._arr[t] = (k, v)
                return self
            else:
                (k1,v1) = self._arr[t]
                if k1 == k:
                    self._arr[t] = (k, v)
                    return self
                else:
                    t = t + 1
        raise KeyError('Out of bounds')
    def get(self, k):
        t = self.hashit(k)
        while t < self._n:
            if not self._arr[t]:
                return None
            else:
                (k1, v1) = self._arr[t]
                if (k1 == k):
                    return self._arr[t][1]
                else:
                    t = t + 1
        return None
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.nxt = None
    def __repr__(self):
        n = list(self.each())
        return str(n)
        
    def each(self):
        t = self
        while t:
            yield (t.k, t.v)
            t = t.nxt

class LHash(IHash):
    """
    >>> h = LHash(4)
    >>> h.put(1,10)
    [None, [(1, 10)], None, None]
    >>> h.put(1,11)
    [None, [(1, 11)], None, None]
    >>> h.put(2,20)
    [None, [(1, 11)], [(2, 20)], None]
    >>> h.put(0,0)
    [[(0, 0)], [(1, 11)], [(2, 20)], None]
    >>> h.put(4,30)
    [[(0, 0), (4, 30)], [(1, 11)], [(2, 20)], None]
    >>> h.get(2)
    20
    >>> h.get(4)
    30
    """
    def __init__(self, n):
        self._arr = [None] * n
        self._n = n
    def __repr__(self):
        return str(self._arr)
    def hashit(self, i):
        return i % self._n
    def put(self, k, v):
        t = self.hashit(k)
        x = self._arr[t]
        while x:
            if x.k == k:
                x.v = v
                return self
            else:
                if x.nxt == None:
                    x.nxt = Node(k,v)
                    return self
                else:
                    x = x.nxt
        self._arr[t] = Node(k,v)
        return self

    def get(self, k):
        t = self.hashit(k)
        x = self._arr[t]
        if not x: return None
        else:
            while x:
                if x.k == k:
                    return x.v
                else:
                    x = x.nxt
        return self

doctest.testmod()
