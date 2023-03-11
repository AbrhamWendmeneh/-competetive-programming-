class MyStack:

    def __init__(self):
        
        self.emp_stack=[]

    def push(self, x: int) -> None:
        
        self.emp_stack.append(x)

    def pop(self) -> int:
        
        return self.emp_stack.pop()

    def top(self) -> int:
        
        return self.emp_stack[-1]

    def empty(self) -> bool:
        
        if len(self.emp_stack)==0:            
            return True
        
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()