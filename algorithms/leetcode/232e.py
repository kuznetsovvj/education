# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []       

    def push(self, x: int) -> None:
        self.first.append(x)        

    def pop(self) -> int:
        if not self.second:
            self.second = self.first[::-1]
            self.first = []
        return self.second.pop()
        
    def peek(self) -> int:
        if not self.second:
            self.second = self.first[::-1]
            self.first = []
        return self.second[-1]
        
    def empty(self) -> bool:
        return not self.first and not self.second