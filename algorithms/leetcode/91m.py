# https://leetcode.com/problems/decode-ways/

def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        fib = [0 for _ in range(101)]
        fib[0], fib[1] = 1, 1
        for i in range(2, len(fib)):
            fib[i] = fib[i-1] + fib[i-2]
        


        flag_mult = False
        cnt, res = 0, 1
        for i in range(len(s)):
            cnt += 1
            if s[i]== '1' or s[i] == '2':
                flag_mult = True
            else:
                if s[i] in ('7', '8', '9') and i >= 1 and s[i-1] == '2':
                    cnt -= 1
                if s[i] == '0' and s[i-1] not in ('1', '2'):
                    return 0
                if s[i] == '0':
                    cnt -= 2
                flag_mult = False
                res = res * fib[cnt]
                cnt = 0
        if flag_mult:
            res = res * fib[cnt]
        
        return res

assert numDecodings("0") == 0
assert numDecodings("1") == 1
assert numDecodings("37") == 1
assert numDecodings("10") == 1
assert numDecodings("11") == 2
assert numDecodings("26") == 2
assert numDecodings("27") == 1
assert numDecodings("102") == 1
assert numDecodings("126") == 3
assert numDecodings("127") == 2
assert numDecodings("721") == 2
assert numDecodings("12812") == 4
assert numDecodings("2101") == 1