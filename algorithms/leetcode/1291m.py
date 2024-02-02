# https://leetcode.com/problems/sequential-digits

def sequentialDigits(low, high):
    nz = [0, 0, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111]
    st = [0, 0, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
    res = []
    for i in range(2, 10):
        k = st[i]
        while k % 10 != 0:
            if k >= low and k <= high:
                res.append(k)
            if k > high:
                return res
            k += nz[i]
    return res

print(sequentialDigits(10, 1000000000))
print(sequentialDigits(100, 300))
print(sequentialDigits(1000, 13000))         


