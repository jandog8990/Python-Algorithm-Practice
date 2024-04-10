# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    # this is the case where we have 
    # both left/right trees
    left = minDepth(root.left)
    right = minDepth(root.right)

    # if no left exhists, follow right tree
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + right 
    if not root.right:
        return 1 + left 

    return min(left, right)+1

n9 = TreeNode(9, None, None)
n15 = TreeNode(15, None, None)
n7 = TreeNode(7, None, None)
n20 = TreeNode(20, n15, n7)
n3 = TreeNode(3, n9, n20)

res = minDepth(n3)
print(f"Res = {res}")
