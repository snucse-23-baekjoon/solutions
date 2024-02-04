class queue:
    integers = list()
    
    def push(self, num):
        self.integers.append(num)
    
    def pop(self):
        if self.integers:
            return self.integers.pop(0)
        return -1
    
    def size(self):
        return len(self.integers)
    
    def empty(self):
        if self.integers:
            return 0
        return 1
    
    def front(self):
        if self.integers:
            return self.integers[0]
        return -1
    
    def back(self):
        if self.integers:
            return self.integers[-1]
        return -1

import sys

repeat = int(sys.stdin.readline().rstrip())
stk = queue()

for _ in range(repeat):
    operation = sys.stdin.readline().rstrip()
    if "push" in operation :
        stk.push(int(operation.split()[1]))
    elif "pop" == operation:
        print(stk.pop())
    elif "size" == operation:
        print(stk.size())
    elif "empty" == operation:
        print(stk.empty())
    elif "front" == operation:
        print(stk.front())
    elif "back" == operation:
        print(stk.back())