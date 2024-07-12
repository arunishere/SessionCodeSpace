class Queue:   
    def __init__(self, maximum):   
        self.maximum = maximum
        self.values = []

    def enqueue(self, element):
        if self.size() == self.maximum:
            print('Queue is full, cannot add elements')
        else:
            self.values.append(element)

    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.values.pop(0)
  
    def isEmpty(self):
        return len(self.values) == 0
 
    def size(self):
        return len(self.values)
    
    def viewQueue(self):
        return self.values