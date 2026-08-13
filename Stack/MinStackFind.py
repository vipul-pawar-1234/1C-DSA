class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,value):
        self.stack = self.stack + [value]

        if not self.minStack or value <= self.minStack[-1]:
            self.minStack = self.minStack + [value]

    def pop(self):
        top = self.stack[-1]
        
        if self.stack[-1] == self.minStack[-1]:
            self.minStack = self.minStack[:-1]

        
        print(top,": is Deleted")
    
    def top(self):
        self.stack = self.stack + self.stack[:-1]
        print(self.stack[-1],": is Top element")

    def getMin(self):
        print(self.minStack[-1],": is Minimum element")

s = MinStack()
s.push(5)
s.push(2)
s.push(1)
s.push(8)

s.pop()
s.getMin()
s.top()