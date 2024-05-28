'''
1. Defining a Function using def keyword
2. Calling a function (without function Parameters)
3. Defining & Calling a function with Parameters
4. Calling a Function referencing Parameters
5. Defining the Function using Default Parameters


'''








# def areaFunc():
#     print('Rectangle Area Calculator')
#     print('=====================')
#     length = float(input('Enter the Length of a Rectangle: '))
#     breadth = float(input('Enter the breadth of a Rectangle: '))
#     print(f'Area of the Rectange: {length*breadth}')

# areaFunc()


# def mulTable(n):
#     for i in range(1,10):
#         print(n,"X",i,"=",n*i)

# for i in range(1,11):
#     mulTable(i)
#     print('================')


# x**n


# def power(x, n):
#     print(x**n)

# power(n=3, x=2)


# def power(x, n=2):
#     print(x**n)
# power(2, 3)



def area(a, b=None):
    if b == None:
        print(f'Area of the Square: {a*a}')
    else:
        print(print(f'Area of the Rectangle: {a*b}'))


area(5)