import operator as op

def reverse_polish_notation(*pargs):
    '''
    for multiplication, divition, summation, subtraction

    [5, 2, '+'] <-> 5 + 2
    [2, 7, '+', 5, '*'] <-> (2 + 7) * 5
    :return: result
    '''
    stack = []
    operator = {'+': op.add,
                '-': op.sub,
                '*': op.mul,
                '/': op.truediv,
                '//': op.floordiv}
    for token in pargs:
        if isinstance(token, (float, int)):
            stack.append(token)
        else:
            y = stack.pop()
            x = stack.pop()
            z = operator[token](x, y)
            stack.append(z)
    return stack.pop()


def brackets_check(s) -> float:
    ''':key
    ckecks brackets sequence correction
    >>> brackets_check('((()))[][()]')
    True
    >>> brackets_check('()')
    True
    >>> brackets_check('(([()))')
    False
    >>> brackets_check('(')
    False
    '''
    stack = []
    for letter in s:
        if letter not in '()[]':
            continue
        if letter in '([':
            stack.append(letter)
        else:
            assert letter in ')]', f'closing bracket expected, got {letter}'
            if not stack:
                return False
            left = stack.pop()
            right = ')' if left == '(' else ']'
            if right != letter:
                return False
    return True if not stack else False

if __name__ == '__main__':
    a = reverse_polish_notation(2, 3, '-', -5, '*')
    print(a, end=f'\n{"-"*50}\n')
    import doctest
    doctest.testmod(verbose=True)