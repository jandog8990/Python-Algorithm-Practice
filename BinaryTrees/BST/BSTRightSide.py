from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# view the right side of binary tree
def rightSideView(root: TreeNode) -> list[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])
    while queue:
        curr_len = len(queue)
        if curr_len > 0:
            val = queue[-1].val
            ans.append(val)   # rightmost node val

        for _ in range(curr_len):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

n5 = TreeNode(5, None, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, n4, n5)
n2 = TreeNode(2, None, None)
root = TreeNode(1, n2, n3)
res = rightSideView(root)
print(f"Ans = {res}")
