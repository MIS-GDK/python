class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:
    """二叉搜索树插入操作"""

    def insert(self, root: TreeNode, val):
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    """二叉搜索树搜索操作"""

    def search(self, root: TreeNode, val):
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.search(root.left, val)
        elif val > root.val:
            return self.search(root.right, val)

    """查找二叉搜索树中最小值点"""

    def findmin(self, root: TreeNode):
        if root.left:
            return self.findmin(root.left)
        else:
            return root

    """查找二叉搜索树中最大值点"""

    def findmax(self, root: TreeNode):
        if root.right:
            return self.findmax(root.right)
        else:
            return root

    """删除二叉搜索树中值为val的点"""

    def delnode(self, root: TreeNode, val):
        if root == None:
            return
        if val < root.val:
            root.left = self.delnode(root.left, val)
        elif val > root.val:
            root.right = self.delnode(root.right, val)
        else:
            # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
            if root.left and root.right:
                temp = self.findmin(root.right)
                root.val = temp.val
                root.right = self.delnode(root.right, temp.val)
            elif root.left == None and root.right == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right

        return root

    # 打印二叉搜索树(中序打印，有序数列)
    def printTree(self, root: TreeNode):
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end=" ")
        self.printTree(root.right)


if __name__ == "__main__":
    List = [17, 5, 35, 2, 11, 29, 38, 9, 16, 8]
    root = None
    op = BinarySearchTree()
    for val in List:
        root = op.insert(root, val)
    print("中序打印二叉搜索树：", end=" ")
    op.printTree(root)
    print("")
    print("根节点的值为：", root.val)
    print("树中最大值为:", op.findmax(root).val)
    print("树中最小值为:", op.findmin(root).val)
    print("查询树中值为5的节点:", op.search(root, 5))
    print("查询树中值为100的节点:", op.search(root, 100))
    print("删除树中值为16的节点:", end=" ")
    root = op.delnode(root, 16)
    op.printTree(root)
    print("")
    print("删除树中值为5的节点:", end=" ")
    root = op.delnode(root, 5)
    op.printTree(root)
    print("")
