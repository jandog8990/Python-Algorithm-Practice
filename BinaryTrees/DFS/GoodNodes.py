# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countGoodNodes(root: TreeNode) -> int:
    def dfs(node, max_so_far):
        if not node:
            return 0

        left = dfs(node.left, max(node.val, max_so_far))
        right = dfs(node.right, max(node.val, max_so_far))
        ans = left + right
        if node.val >= max_so_far:
            ans += 1

        return ans
    
    return dfs(root, float("-inf"))

n7 = TreeNode(7, None, None)
n2 = TreeNode(2, None, None)
n11 = TreeNode(11, n7, n2)
n41 = TreeNode(4, n11, None)

n1 = TreeNode(1, None, None)
n42 = TreeNode(4, None, n1)
n13 = TreeNode(13, None, None)
n8 = TreeNode(8, n13, n42)

n5 = TreeNode(5, n41, n8)
count = countGoodNodes(n5)
print(f"Count = {count}")
