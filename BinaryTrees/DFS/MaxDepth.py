# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# find the max depth of a binary tree uses DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        maxlr = max(left,right)

        return maxlr + 1

n3 = TreeNode(3, None, None)
n4 = TreeNode(4, None, None)
n6 = TreeNode(6, None, None)
n5 = TreeNode(5, None, n6)
n2 = TreeNode(2, None, n5)
n1 = TreeNode(1, n3, n4)
n0 = TreeNode(0, n1, n2)

sol = Solution()
res = sol.maxDepth(n0)
print(f"Res = {res}")
