from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def for min lambda
def min_lambda():
    return lambda x: (abs(target-x), x)

# find the closest value in the tree to the input
# val given (this is a BST problem at each level)
def findClosestVal(root: TreeNode, target: float) -> list[int]:
    closest = root.val

    while root:
        # calculate the closest by feeding root and closest to absolute diff 
        closest = min(root.val, closest, key=lambda x: abs(target-x))
        root = root.left if target < root.val else root.right

    return closest

# create new tree 
n1 = TreeNode(1, None, None)
n3 = TreeNode(3, None, None)
n5 = TreeNode(5, None, None)
n2 = TreeNode(2, n1, n3)
root = TreeNode(4, n2, n5)
closest = findClosestVal(root, 3.143) 
print(f"closest = {closest}")
print("\n")
