import doctest

def pparse(lst):
    """
    >>> pparse('')
    ''
    >>> pparse('A')
    'A'
    >>> pparse('A B')
    'A B'
    >>> pparse('A + B')
    'A B +'
    >>> pparse('A + B * C')
    'A B C * +'
    >>> pparse('( A + B ) * C')
    'A B + C *'
    >>> pparse('( A + B * C ) * D')
    'A B C * + D *'
    """
    opStack = list()
    output = list()
    for i in lst.split():
        if i in 'ABCD':
            output.append(i)
        elif i == '(':
            opStack.append(i)
        elif i == ')':
            while True:
                a = opStack.pop()
                if a == '(': break
                else:
                    output.append(a)
        elif i in ['*', '+']:
            opStack.append(i)
        else:
            raise ValueError('>%s<' % i)
    opStack.reverse()
    return ' '.join(output + opStack)
    
doctest.testmod()

