class Dequeue:
    integers = list()
    
    def push_front(self, num):
        self.integers = [num] + self.integers
        
    def push_back(self, num):
        self.integers = self.integers + [num]
    
    def pop_front(self):
        if self.integers:
            return self.integers.pop(0)
        return -1
    
    def pop_back(self):
        if self.integers:
            return self.integers.pop(-1)
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
stk = Dequeue()

for _ in range(repeat):
    operation = sys.stdin.readline().rstrip()
    if "push" in operation :
        if "front" in operation:
            stk.push_front(int(operation.split()[1]))
        else:
            stk.push_back(int(operation.split()[1]))
    elif "pop" in operation:
        if "front" in operation:
            print(stk.pop_front())
        else:
            print(stk.pop_back())
    elif "size" == operation:
        print(stk.size())
    elif "empty" == operation:
        print(stk.empty())
    elif "front" == operation:
        print(stk.front())
    elif "back" == operation:
        print(stk.back())