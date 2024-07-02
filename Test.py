# from stack import Stack

# elements = ['a'+ str(i) for i in range(8)]

# s = Stack()

# for element in elements:

#     s.push(element)


# print(s.pop())


# print(elements)

from queuemain import Queue


q = Queue(10)

elements = ['a'+ str(i) for i in range(12)]

for ele in elements:

    q.enqueue(ele)

print(q.viewQueue())

print(q.dequeue())

print(q.viewQueue())

q.enqueue('a20')

print(q.viewQueue())

q.enqueue('a21')

# while not q.isEmpty():

#     print(q.dequeue())