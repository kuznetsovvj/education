# https://leetcode.com/problems/multiply-strings/
# leetcode 43
# medium

def multiply(num1, num2):
    res = []
    for idx1, item1 in enumerate(num1[::-1]):
        value1 = int(item1)
        reg = 0
        for idx2, item2 in enumerate(num2[::-1]):
            value2 = int(item2)
            while len(res) <= idx1 + idx2:
                res.append(0)
            old_reg = reg
            reg = (res[idx1 + idx2] + value1 * value2 + reg) // 10
            res[idx1 + idx2] = (res[idx1 + idx2] + value1 * value2 + old_reg) % 10
        z = 0
        while reg > 0:
            while len(res) <= idx1 + len(num2) + z:
                res.append(0)
            res[idx1 + len(num2) + z] = reg % 10
            reg = reg // 10
            z += 1
    res = list(map(str, res))
    while len(res) > 1 and res[-1] == '0':
        del res[-1]
    return ''.join(res[::-1])


#assert int(multiply("1", "3")) == 3
#assert int(multiply("11", "22")) == 11 * 22
#assert int(multiply("18", "9")) == 18 * 9
#assert int(multiply("230", "45234")) == 230 * 45234
assert multiply("0", "34434") == "0"


