# https://leetcode.com/problems/same-tree/description/

# easy

def isSameTree(p, q):
    def check(v1, v2):
        if v1 is None and v2 is None:
            return True
        if v1 is None or v2 is None:
            return False
        if v1.val != v2.val:
            return False
        if (v1.left is None) != (v2.left is None):
            return False
        if (v1.right is None) != (v2.right is None):
            return False
        left_result, right_result = True, True
        if v1.left:
            left_result = check(v1.left, v2.left)
        if v1.right:
            right_result = check(v1.right, v2.right)
        return True and left_result and right_result

    return check(p, q)
