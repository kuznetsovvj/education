# https://leetcode.com/problems/find-first-palindromic-string-in-the-array

def firstPalindrome(words):
    for w in words:
        f = True
        for i in range(len(w) // 2 ):
            if w[i] != w[len(w) - 1 - i]:
                f = False
                break
        if f:
            return w
    return ""
