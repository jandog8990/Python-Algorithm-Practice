from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# insert new node into the tree based on 
# BST rules (left < node < right)
def insertNode(root: TreeNode, val: int) -> TreeNode:
    if not root:
        # this will create a new node at the leaf 
        return TreeNode(val) 

    if val > root.val:
        print(f"val > root.val : {val} > {root.val}") 
        root.right = insertNode(root.right, val)
    else:
        print(f"val < root.val : {val} < {root.val}") 
        root.left = insertNode(root.left, val)
    print("\n")

    return root

def bst_print(node: TreeNode):
    queue = deque([node])
    while queue:
        curr_queue = queue
        queue = deque()
        for node in curr_queue:
            print(f"curr node val = {node.val}")
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)

n1 = TreeNode(1, None, None)
n3 = TreeNode(3, None, None)
n7 = TreeNode(7, None, None)
n2 = TreeNode(2, n1, n3)
root = TreeNode(4, n2, n7)
new_tree = insertNode(root, 5)
print(f"New tree: {new_tree}")
bst_print(new_tree) 
