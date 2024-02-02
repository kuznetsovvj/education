# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

def findLength(nums1, nums2):
    r = [[-1 for _ in range(len(nums1))] for _ in range(len(nums2))]
    mx = 0
    for i in range(len(nums2)):
        if nums1[0] == nums2[i]:
            r[i][0] = 1
            mx = 1
        else:
            r[i][0] = 0
    
    for j in range(len(nums1)):
        if nums2[0] == nums1[j]:
            r[0][j] = 1
            mx = 1
        else:
            r[0][j] = 0
            
    for i in range(1, len(nums2)):
        for j in range(1, len(nums1)):
            if nums2[i] == nums1[j]:
                r[i][j] = r[i-1][j-1] + 1
                mx = max(mx, r[i][j])
            else:
                r[i][j] = 0
    
    return mx

print(findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))