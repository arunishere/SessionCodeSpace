from stack import Stack

elements = ['a'+ str(i) for i in range(8)]

s = Stack()

for element in elements:

    s.push(element)


print(s.pop())


# print(elements)


