# https://leetcode.com/problems/leaf-similar-trees/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, res):
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(root.val)
            return res
        if root.left is not None:
            res = self.check(root.left, res)
        if root.right is not None:
            res = self.check(root.right, res)
        return res
        
    def leafSimilar(self, root1, root2) -> bool:
        res1 = self.check(root1, [])
        res2 = self.check(root2, [])
        if len(res1) != len(res2):
            return False
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                return False
        return True