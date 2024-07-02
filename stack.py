class Stack:

    def __init__(self):

        self.values = []

    def push(self, element):

        self.values.append(element)

    def pop(self):

        if self.isEmpty():
            print('The Stack is Empty')

        else:            
            return self.values.pop()
    
    def isEmpty(self):

        return len(self.values) == 0
    
    def viewStack(self):

        print(self.values)

    def size(self):

        return len(self.values)