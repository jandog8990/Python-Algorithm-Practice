class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def dfs(node: TreeNode):
    print(f"Node = {node.val}") 
    if node == None:
        return
    
    # recursion to the left side and right
    dfs(node.left)
    dfs(node.right)
    return
   
def preorder(node: TreeNode):
    if node == None:
        return

    print(f"node = {node.val}")
    preorder(node.left)
    preorder(node.right)
    return

def inorder(node: TreeNode):
    if node == None:
        return

    inorder(node.left)
    print(f"node = {node.val}")
    inorder(node.right)
    return

def postorder(node: TreeNode):
    if node == None:
        return

    postorder(node.left)
    postorder(node.right)
    print(f"node = {node.val}")
    return

n1 = TreeNode(6, None, None)
n2 = TreeNode(4, None, n1)
n3 = TreeNode(3, None, None)
n4 = TreeNode(1, n3, n2)
n5 = TreeNode(5, None, None)
n6 = TreeNode(2, None, n5)
n7 = TreeNode(0, n4, n6)

print("Preorder")
preorder(n7)
print("\n")

print("Inorder")
inorder(n7)
print("\n")

print("Postorder")
postorder(n7)
print("\n")

