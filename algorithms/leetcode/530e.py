# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.m = list()
        self.check(root)
        self.m.sort()
        c = self.m[1] - self.m[0]
        for i in range(2, len(self.m)):
            c = min(c, self.m[i] - self.m[i-1])
        return c

    def check(self, vertex):
        if vertex is None:
            return
        self.m.append(vertex.val)
        if vertex.left is not None:
            self.check(vertex.left)
        if vertex.right is not None:
            self.check(vertex.right)