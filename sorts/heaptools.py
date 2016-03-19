
def isheap(items, root=0, size=-1):
    """maxheap"""
    if size == -1:
        size = len(items)
    if size <= 1:
        return True
    return all(items[i] <= items[(i - 1) // 2] for i in range(1, size) if i >= root)


def mark(A):
    A = A.copy()
    print('a: ',A)
    B = []
    A[0] = 0
    for i in range(1, len(A)): A[i] = (i - 1) // 2
    print('p: ',A)
    for i in range(0, len(A)): B.append(i)
    print('i: ',B)


def check(items, root=0, size=-1):
    if size == -1:
        size = len(items)
    if size <= 1:
        return True
    if not isheap(items, root, size):
        mark(items)
        raise ValueError('X %s root:%i size:%i' % (items, root, size))

