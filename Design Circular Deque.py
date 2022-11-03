class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max = k

        self.data = [None]*self.max

        self.size = 0

        self.rear = 0

        self.front = 0       

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        self.front = (self.front - 1 +self.max) % self.max
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False

        self.data[self.rear] = value

        self.rear = (self.rear + 1) % self.max

        self.size += 1

        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): return False

        self.data[self.front] = None

        self.front = (self.front + 1) % self.max

        self.size -=1

        return True       

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.rear = (self.rear - 1 +self.max) % self.max
        self.data[self.rear]=None
        self.size -=1
        return True
       
    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.data[self.front]
        
    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1

        return self.data[self.rear-1]  
     
    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        
    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.max
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
