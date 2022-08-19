# https://codeforces.com/contest/1714/problem/E

def check(nums):
    r = create_avalaible(nums[0])
    for num in nums:
        t = create_avalaible(num)
        if len(r & t) > 0:
            continue
        else:
            return False
    return True
        
def create_avalaible(num):
    result = set()
    result.add(num)
    # 0 и 5
    if num % 5 == 0:
        result.add(num + (num % 10))
        return result
    # все остальное
    num += (num % 10) % 20
    while num not in result:
        result.add(num % 20)
        num = (num + (num % 10)) % 20
    return result


t = int(input())
for _ in range(t):
    input()
    res = check(tuple(map(int, input().split())))
    if res:
        print("YES")
    else:
        print("NO")
