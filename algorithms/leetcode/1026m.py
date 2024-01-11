# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# beats 92.9% python solutions, kek

class Solution:
    def check(self, maxstack, minstack, root, maxvalue):
        # проверить maxvalue для текущей ноды
        maxvalue = max(maxvalue, abs(maxstack[-1] - root.val), abs(minstack[-1] - root.val))
       
        if root.val >= maxstack[-1]:
            maxstack.append(root.val)
        if root.val <= minstack[-1]:
            minstack.append(root.val)
        
        # проверить левый наследник
        if root.left is not None:
            maxstack, minstack, leftvalue = self.check(maxstack, minstack, root.left, maxvalue)
            maxvalue = max(maxvalue, leftvalue)
        # проверить правый наследник
        if root.right is not None:
            maxstack, minstack, rightvalue = self.check(maxstack, minstack, root.right, maxvalue)
            maxvalue = max(maxvalue, rightvalue)

        # удалить свои значения из стека
        if root.val == maxstack[-1]:
            del maxstack[-1]
        if root.val == minstack[-1]:
            del minstack[-1]

        # вернуть ответ
        return (maxstack, minstack, maxvalue) 
    

    def maxAncestorDiff(self, root) -> int:
        maxstack, minstack = [root.val], [root.val]
        maxvalue = 0
        maxstack, minstack, maxvalue = self.check(maxstack, minstack, root, maxvalue)
        return maxvalue