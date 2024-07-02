class Queue:
    
    def __init__(self):

        self.values = []

    def enqueue(self, element):


        self.values.append(element)


    def dequeue(self):


        return self.values.pop(0)