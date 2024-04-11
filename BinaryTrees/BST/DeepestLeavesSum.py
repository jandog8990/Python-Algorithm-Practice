# get the total sum of the deepest leaves
from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: TreeNode) -> int:
    def maxDepth(node: TreeNode) -> int:
        if not node:
            return 0

        # get max of left subtrees and right
        left = maxDepth(node.left)
        right = maxDepth(node.right)
        maxlr = max(left, right)

        return maxlr + 1

    # if root DNE 
    if not root:
        return 0

    # get total numbers then calculate the sum
    num_layers = maxDepth(root)
    count = 1
    queue = deque([root])
    while queue:
        curr_len = len(queue)

        if count == num_layers:
            # calc sum of queue
            total_sum = 0 
            for _ in range(curr_len):
                total_sum += queue.popleft().val
            return total_sum

        # loop through each layer of nodes
        for _ in range(curr_len):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # count the number of layers
        count += 1

n5 = TreeNode(5, None, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, n4, n5)
n2 = TreeNode(2, None, None)
root = TreeNode(1, n2, n3)
res = deepestLeavesSum(root)
print(f"Ans = {res}")
