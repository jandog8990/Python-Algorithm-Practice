from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# deepest leaves sum using BFS and deque
def deepestLeavesSum(root: TreeNode) -> int:
    queue = deque([root,])

    while queue:
        curr_queue = queue
        curr_len = len(queue)
        # this is important as it doesn't mutate the queue 
        queue = deque()

        for node in curr_queue: 

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print("Current queue:")
    print(list(curr_queue))
    print("\n")
    return sum([node.val for node in curr_queue])

n5 = TreeNode(5, None, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, n4, n5)
n2 = TreeNode(2, None, None)
root = TreeNode(1, n2, n3)
res = deepestLeavesSum(root)
print(f"Ans = {res}")
