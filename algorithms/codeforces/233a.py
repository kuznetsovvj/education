# https://codeforces.com/problemset/problem/233/A

def check(n):
    if n % 2 == 1:
        return "-1"
    else:
        res = []
        i = 2
        for _ in range(n//2):
            res.append(i)
            i -= 1
            res.append(i)
            i += 3
            
        return ' '.join(map(str, res))

print(check(int(input())))