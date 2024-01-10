# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, mtx, node):
        if node is None:
            return mtx
        
        if node.val not in mtx:
            mtx[node.val] = set()

        if node.left is not None:
            if node.left.val not in mtx:
                mtx[node.left.val] = set()
            mtx[node.left.val].add(node.val)
            mtx[node.val].add(node.left.val)
            mtx = self.check(mtx, node.left)
    
        if node.right is not None:
            if node.right.val not in mtx:
                mtx[node.right.val] = set()
            mtx[node.right.val].add(node.val)
            mtx[node.val].add(node.right.val)
            mtx = self.check(mtx, node.right)
        
        return mtx
        
            
    def amountOfTime(self, root, start: int) -> int:
        mtx = {}
        mtx = self.check(mtx, root)
        current_gen = set()
        current_gen.add(start)
        next_gen = set()
        j = 0
        while True:
            for t in current_gen:
                for i in mtx[t]:
                    next_gen.add(i)
                    mtx[i].remove(t)
                del mtx[t]
            if len(next_gen) == 0:
                return j
            current_gen = next_gen
            next_gen = set()
            j += 1