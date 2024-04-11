from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# validate that the given tree is a BST
# the small, large are updated at each step
def isValidBST(root: TreeNode) -> bool:
    def dfs(node, small, large):
        if not node:
            return True

        if not (small < node.val < large):
            return False

        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)

        return left and right
    
    return dfs(root, float("-inf"), float("inf"))

n23 = TreeNode(23, None, None)
n8 = TreeNode(8, None, None)
n2 = TreeNode(2, None, None)
n5 = TreeNode(5, n2, n8)
n12 = TreeNode(12, None, n23)
root = TreeNode(10, n5, n12)
res = isValidBST(root)
print(f"Valid = {res}")
