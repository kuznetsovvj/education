# https://leetcode.com/problems/palindromic-substrings/

def countSubstring(s):
    # по столбцам (первый индекс) - индекс начало палиндрома
    # по строкам (второй индекс) - индекс конца палиндрома
    d = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        # один символ всегда палиндром
        d[i][i] = True
        for j in range(i):
            # если конец раньше начала - False
            d[i][j] = False
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if j == i + 1:
                d[i][j] = s[i] == s[j]
            else:
                if d[i+1][j-1] == True and s[i] == s[j]:
                    d[i][j] = True
                else:
                    d[i][j] = False
    r = 0
    for i in range(len(s)):
        for j in range(len(s)):
            r += d[i][j]
    
    return r

print(countSubstring("abc"))
print(countSubstring("aaa"))


