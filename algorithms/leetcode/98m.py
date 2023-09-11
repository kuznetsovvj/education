# https://leetcode.com/problems/validate-binary-search-tree/

def isValidBST(root):
    return check(root)

def check(root, top_limit=float('inf'), bottom_limit=float('-inf')):
    if root.val >= top_limit or root.val <= bottom_limit:
        return False
    left, right = True, True
    if root.left:
        left = check(root.left, root.val, bottom_limit)
    if root.right:
        right = check(root.right, top_limit, root.val)
    return left and right

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

c = TreeNode(3,None,None)
b = TreeNode(1,None,None)
a = TreeNode(2,b,c)

print(isValidBST(a))