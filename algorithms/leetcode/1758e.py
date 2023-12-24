# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

def minOperations(s):
    odd, even = {"1":0, "0":0}, {"1":0, "0":0}
    for idx, item in enumerate(s):
        if idx % 2 == 0:
            odd[item] += 1
        else:
            even[item] += 1
    return min(odd["1"] + even["0"], odd["0"] + even["1"])


assert minOperations("0100") == 1
assert minOperations("10") == 0
assert minOperations("1111") == 2
