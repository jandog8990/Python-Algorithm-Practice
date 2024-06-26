# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return True

    if p == None or q == None:
        return False

    if p.val != q.val:
        return False

    if p.val == q.val:
        return True

    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)
    return left and right
