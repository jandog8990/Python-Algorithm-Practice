from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# find the min difference between adjacent
# nodes within the BST
def getMinDifference(root: TreeNode) -> int:
    def preorder_dfs(node:TreeNode):
        if not node:
            return

        values.append(node.val)
        left = preorder_dfs(node.left)
        right = preorder_dfs(node.right)

    def inorder_dfs(node:TreeNode):
        if not node:
            return

        left = inorder_dfs(node.left)
        values.append(node.val)
        right = inorder_dfs(node.right)

    def postorder_dfs(node:TreeNode):
        if not node:
            return

        left = postorder_dfs(node.left)
        right = postorder_dfs(node.right)
        values.append(node.val)

    values = []
    diff = float("inf") 
    #preorder_dfs(root)
    inorder_dfs(root)
    #postorder_dfs(root)
    for i in range(1, len(values)):
        diff = min(diff, values[i]-values[i-1])
    return diff 

n1 = TreeNode(1, None, None)
n7 = TreeNode(7, None, None)
n5 = TreeNode(5, n1, n7)
n15 = TreeNode(15, None, None)
root = TreeNode(9, n5, n15)
res = getMinDifference(root)
print(f"Ans = {res}")
