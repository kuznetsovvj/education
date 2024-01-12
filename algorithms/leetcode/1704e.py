# https://leetcode.com/problems/determine-if-string-halves-are-alike

def halvesAreAlike(s: str) -> bool:
        vw = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        cnt = 0
        i = len(s) // 2
        for j in range(len(s)):
            if s[j] in vw:
                if j < i:
                    cnt += 1
                else:
                    cnt -=1
        if cnt == 0:
            return True
        return False