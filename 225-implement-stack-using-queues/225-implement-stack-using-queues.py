class MyStack:

    def __init__(self):
        self.queue=deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        '''the case that I use is that for the values to return or to push it out i try to iterate through the loop and then by removing all the values of the given data and finding the last element in the queue and append it to the first defined queue and then i return it back'''
        
        for i in range(len(self.queue)-1):
            
            self.queue.append(self.queue.popleft())
            
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()