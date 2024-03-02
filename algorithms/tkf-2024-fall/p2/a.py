
class MinStack():
    def __init__(self):
        self.stack = []
        self.mnstack = []
    
    def add(self, value):
        self.stack.append(value)
        if not len(self.mnstack) or self.mnstack[-1] >= value:
            self.mnstack.append(value)
    
    def detele(self):
        last = self.stack.pop()
        if self.mnstack[-1] == last:
            self.mnstack.pop()
    
    def getmin(self):
        return self.mnstack[-1]
    

a = MinStack()
for _ in range(int(input())):
    s = tuple(map(int, input().split()))
    if s[0] == 1:
        a.add(s[1])
        continue
    if s[0] == 2:
        a.detele()
        continue
    if s[0] == 3:
        print(a.getmin())
              