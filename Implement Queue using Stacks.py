class MyQueue(object):

    def __init__(self):
        self.items=[]
        self.stack_2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack_2:

            return self.stack_2.pop()

        else:

            while self.items:

                self.stack_2.append(self.items.pop())

            return self.stack_2.pop()                   

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_2:

            return self.stack_2[-1]

        else:        

            while self.items:

                self.stack_2.append(self.items.pop())

            return self.stack_2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.items and not self.stack_2

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
