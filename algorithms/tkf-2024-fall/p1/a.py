input()
nums = set(map(int, input().split()))
req = tuple(map(int, input().split()))
for r in req:
    if r in nums:
        print("YES")
    else:
        print("NO")

# Можно сделать через import bisect и проверку r == nums[bisect.left(nums, r)]
# Можно и самому написать бинарный поиск самому, но это ужасно скучно  