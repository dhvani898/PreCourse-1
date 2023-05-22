# Implment Stack using Array
# Time Complexity :O(N)
class Stack:

    def _init_(self):
        self.stack = []
        self.topi = -1

    def push(self, val: int) -> None:
        self.topi +=1
        self.stack.append(val)
        
    def pop(self) -> None:
        self.topi -=1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[self.topi]
        
    def size(self):
        return len(self.stack)
    
    def show(self):
        for i in range(self.topi,-1,-1):
            print(self.stack[i])
    
    def isEmpty():
        if self.topi ==-1:
            print("Stack is Empty")
        else:
            print("Stack is not empty")