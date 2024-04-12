# get the total sum of the deepest leaves
from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# given a range find the sum of all nodes within the range
# ensure you use BST to remove left/right trees
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    if not root:
        return 0

    ans = 0
    if low <= root.val <= high:
        # first check the current node val in range
        ans += root.val
    if low < root.val:
        # low < nodeVal => there exists vals in left 
        # subtree that might be within the range
        ans += rangeSumBST(root.left, low, high)
    if high > root.val:
        # high > nodeVal => there exists vals in right
        # subtree that might be within the range
        ans += rangeSumBST(root.right, low, high)

    return ans

# create the tree
n18 = TreeNode(18, None, None)
n7 = TreeNode(7, None, None)
n3 = TreeNode(3, None, None)
n15 = TreeNode(15, None, n18)
n5 = TreeNode(5, n3, n7)
root = TreeNode(10, n5, n15)
res = rangeSumBST(root, 7, 15)
print(f"Sum = {res}")
