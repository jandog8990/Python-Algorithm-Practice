from collections import deque
# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print all nodes for deque
def print_all_nodes(root: TreeNode):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # logic at the current level

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            print(node.val)

            # put next level on queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

n5 = TreeNode(5, None, None)
n2 = TreeNode(2, None, n5)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, None, None)
n1 = TreeNode(1, n3, n4)
root = TreeNode(0, n1, n2)
print_all_nodes(root)
