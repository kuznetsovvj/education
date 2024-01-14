# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def check(self, w):
        cnt = {}
        for it in w:
            if it not in cnt:
                cnt[it] = 1
            else:
                cnt[it] += 1
        return cnt

    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = self.check(word1)
        cnt2 = self.check(word2)
        c1 = list(cnt1.values())
        c1.sort()
        c2 = list(cnt2.values())
        c2.sort()
        if set(cnt1.keys()) != set(cnt2.keys()):
            return False
        if len(c1) != len(c2):
            return False
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                return False
        return True        


