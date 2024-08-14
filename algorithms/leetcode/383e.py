# https://leetcode.com/problems/ransom-note/

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter


        a = Counter(ransomNote)
        b = Counter(magazine)
        for k, v in a.items():
            if k in b and a[k] <= b[k]:
                continue
            else:
                return False
        return True
        