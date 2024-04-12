from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: TreeNode) -> list[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    count = 0 
    while queue:
        curr_len = len(queue)
        curr_max = float("-inf")    # largest val for curr level

        for _ in range(curr_len):
            node = queue.popleft()
            curr_max = max(curr_max, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        count += 1        
        ans.append(curr_max)
    print(f"Number of layers = {count}")

    return ans

n5 = TreeNode(5, None, None)
n4 = TreeNode(3, None, None)
n9 = TreeNode(9, None, None)
n3 = TreeNode(3, n5, n4)
n2 = TreeNode(2, None, n9)
root = TreeNode(1, n3, n2)
res = largestValues(root)
print(f"Ans = {res}")

