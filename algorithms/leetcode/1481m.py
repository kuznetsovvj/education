# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

def findLeastNumOfUniqueInts(arr, k):
    from collections import Counter
    c = Counter(arr)
    t = list(c.values())
    t.sort(reverse=True)
    while k > 0:
        if len(t) > 0:
            if t[-1] <= k:
                k -= t[-1]
                del t[-1]
            else:
                break
        else:
            return 0
    return len(t)

#print(findLeastNumOfUniqueInts([5,5,4], 1))
print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
