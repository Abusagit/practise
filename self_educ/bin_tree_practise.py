from structures.my_tree import BinaryTree
from structures.my_stack import Stack
import operator


'''Parse tree'''


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    currentTree = tree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('(')
            stack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            stack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = stack.pop()

        else:
            try:
                currentTree.setRootVal(int(i))
                parent = stack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError(f'token {i} isn`t valid integer')

    return tree


def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        f = opers[parseTree.getRootVal()]
        return f(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()  # we are in the leaf node which is integer so return it


'''Tree traversals'''


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    # res1 = None
    # res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()


def recover_exp(tree):
    sVal = ''
    if tree:
        sVal = '(' + recover_exp(tree.getLeftChild()) + str(tree.getRootVal()) + recover_exp(tree.getRightChild()) + ')'
        # sVal = recover_exp(tree.getLeftChild())
        # sVal += str(tree.getRootVal())
        # sVal += recover_exp(tree.getRightChild())

    return sVal


if __name__ == '__main__':
    pt = build_parse_tree('( ( 10 + 5 ) * 3 )')
    print(evaluate(pt))
    preorder(pt)
    print('\n\n')
    postorder(pt)
    print('\n\n')
    inorder(pt)
    print(postordereval(pt))

    print(recover_exp(pt))