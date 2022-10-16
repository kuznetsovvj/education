# https://codeforces.com/contest/1744/problem/A

def check(nums, word):
    s = dict()
    for num, char in zip(nums, word):
        if num not in s:
            s[num] = char
        else:
            if s[num] != char:
                return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    input()
    nums = tuple(map(int, input().split()))
    word = input()
    print(check(nums, word))