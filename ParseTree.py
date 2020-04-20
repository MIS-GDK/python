import queue
import operator
from binaryTree import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = queue.LifoQueue()
    eTree = BinaryTree("")
    pStack.put(eTree)
    currentTree = eTree
    for i in fplist:
        if i == "(":
            currentTree.insertLeft("")
            pStack.put(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ["+", "-", "*", "/", ")"]:
            currentTree.setRootVal(int(i))
            parent = pStack.get()
            currentTree = parent
        elif i in ["+", "-", "*", "/"]:
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.put(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            currentTree = pStack.get()
        else:
            return ValueError

    return eTree


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postordereval(tree):
    opers = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    # inorder(pt)
    # pt.inorder()
    print(postordereval(pt))
