# binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# find the path of nodes that add up
# to the given target sum
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    def dfs(node, curr):
        # if we don't have any subtrees -> return False 
        if not node:
            return False

        # if both left/right are null, then node is leaf
        if node.left == None and node.right == None:
            # return whether the leaf node returns target or NOT 
            curr += node.val 
            print(f"leaf sum = {curr}\n") 
            return curr == targetSum

        # add current node val to total sum
        curr += node.val
        print(f"curr += {node.val} = {curr}") 
        leftVal = node.left.val if node.left else None
        rightVal = node.right.val if node.right else None 
        print(f"left = dfs({leftVal}, {curr})") 
        left = dfs(node.left, curr)
        print(f"right = dfs({rightVal}, {curr})") 
        print("\n") 
        right = dfs(node.right, curr)
      
        print(f"left = {left}")
        print(f"right = {right}")
        print("\n") 
        return left or right
    
    return dfs(root, 0) 
   
n7 = TreeNode(7, None, None)
n2 = TreeNode(2, None, None)
n11 = TreeNode(11, n7, n2)
n41 = TreeNode(4, n11, None)

n1 = TreeNode(1, None, None)
n42 = TreeNode(4, None, n1)
n13 = TreeNode(13, None, None)
n8 = TreeNode(8, n13, n42)

n5 = TreeNode(5, n41, n8)

res = hasPathSum(n5, 22)
print(f"Res = {res}")
