# https://leetcode.com/problems/maximum-distance-in-arrays/

def maxDistance(arrays):
    mx1, mx2 = float('-inf'), float('-inf')
    mn1, mn2 = float('inf'), float('inf')
    mx_idx, mn_idx = -1, -1

    for idx, array in enumerate(arrays):
        #mx
        if array[-1] > mx1:
            mx2 = mx1
            mx1 = array[-1]
            mx_idx = idx
        elif array[-1] == mx1:
            mx_idx = -1
        elif array[-1] > mx2:
            mx2 = array[-1]
        # mn
        if array[0] < mn1:
            mn2 = mn1
            mn1 = array[0]
            mn_idx = idx
        elif array[0] == mn1:
            mn_idx = -1
        elif array[0] < mn2:
            mn2 = array[0]
        
    if (mn_idx == -1) or (mx_idx == -1) or (mn_idx != mx_idx):
        return mx1 - mn1
    
    return max(mx2 - mn1, mx1 - mn2)