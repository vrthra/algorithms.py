
import doctest

class Node:
    def __init__(self,i):
        self.data = i
        self.nxt = None
    def __repr__(self):
        return str(self.data)

class MyList:
    """
    >>> l = MyList()
    >>> l.isEmpty()
    True
    >>> l.add(1)
    >>> l.isEmpty()
    False
    >>> l.add(2)
    >>> l.add(3)
    >>> l.add(4)
    >>> l.size()
    4
    >>> l.search(3).data
    3
    >>> list(l.remove(3).each())
    [4, 2, 1]
    >>> list(l.remove(3).each())
    [4, 2, 1]
    >>> l.append(0)
    [4, 2, 1, 0]
    >>> l.remove(2)
    [4, 1, 0]
    >>> l.insert_after(4,3)
    [4, 3, 1, 0]
    >>> l.insert_before(1,2)
    [4, 3, 2, 1, 0]
    """
    def __init__(self):
        self._head = None
    def __repr__(self):
        return str([i for i in self.each()])
    
    def add(self,item):
        node = Node(item)
        node.nxt = self._head
        self._head = node
    def isEmpty(self):
        return self._head == None
    def each(self):
        h = self._head
        while h:
            n = h.nxt
            yield h
            h = n
    def size(self):
        return len(list(self.each()))
    def search(self, item):
        for i in self.each():
            if i.data == item:
                return i
    def remove(self, item):
        h = self._head
        if h.data == item:
            self._head = h.nxt
            return self
        while h:
            if h.nxt and h.nxt.data == item:
                h.nxt = h.nxt.nxt
                return self
            h = h.nxt
        return self
    def append(self,item):
        v = list(self.each())[-1]        
        v.nxt = Node(item)
        return self
    def insert_after(self, item, value):
        v = self.each()
        x = next(v)
        while x:
            if x.data == item:
                n = Node(value)
                n.nxt = x.nxt
                x.nxt = n
            x = next(v, None)
        return self
    def insert_before(self, item, value):
        v = self.each()
        x = next(v, None)
        last = self._head
        if self._head.data == item:
            self._head = Node(n)
            self._head.nxt = last
            return self
        while x:
            if x.data == item:
                n = Node(value)
                last.nxt = n
                n.nxt = x
                return self
            last = x
            x = next(v, None)
        return self
    
doctest.testmod(verbose=False)
