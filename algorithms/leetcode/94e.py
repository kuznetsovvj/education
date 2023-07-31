# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def contact(res, pipe):
            t = pipe.pop()
            if t.left != None:
                pipe.append(t.left)
            if len(pipe):
                contact(res, pipe)
            res.append(t.val)
            if t.right != None:
                pipe.append(t.right)
            if len(pipe):
                contact(res, pipe)


        res = []
        if root != None:
            pipe = [root]
            contact(res, pipe)

        return res
