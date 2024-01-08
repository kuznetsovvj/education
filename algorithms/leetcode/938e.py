# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, res, root, low, high):
        if root is None:
            return res
        if root.val < low:
            return res + self.check(res, root.right, low, high)
        if root.val > high:
            return res + self.check(res, root.left, low, high)
        return res + self.check(res, root.right, low, high) + self.check(res, root.left, low, high) + root.val

    def rangeSumBST(self, root, low, high):
        res = 0
        return self.check(res, root, low, high)