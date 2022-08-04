# https://leetcode.com/problems/merge-sorted-array/
# easy

def merge(nums1, m, nums2, n):
    crt = m + n + 1
    crt1 = m - 1
    crt2 = n - 1
    while crt >= 0:
        if crt1 >= 0 and crt2 >= 0:
            nums1[crt] = max(nums1[crt1], nums2[crt2])
            if nums1[crt] == nums1[crt1]:
                crt1 -= 1
            else:
                crt2 -= 1
        else:
            if crt1 >= 0:
                nums1[crt] = nums1[crt1]
                crt1 -= 1
            else:
                nums1[crt] = nums2[crt2]
                crt2 -= 1
        crt -= 1