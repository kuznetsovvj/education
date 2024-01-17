# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        import collections
        c = collections.Counter(arr)
        return len(set(c.values())) == len(c.values())