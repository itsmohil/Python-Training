# Example 1
# def func(i, j):
#     print(i, j)
# func(10, 20)  # Positional Arguments
# func(j = 20, i = 10)  # Keyword Arguments

# Example 2 Default values assigned to positional arguments
# def func(i, j=10):
#     print(i, j)
# func(100, 200)  # 100 200
# func(100)  # 100 10-Default values to the positional arguments

# Example 3 Keyword arguments
# def greetings(name, greetmsg):
#     print(greetmsg + " " + name)
# greetings(name="John", greetmsg="Hello")
# greetings(greetmsg="Hello", name="John")

# Example 4 Mix positional and keyword arguments
# def myfunc(a, b, c):
#     print(a, b, c)
# myfunc(10, 20, 30)  # Positional arguments
# myfunc(a = 10, b = 20, c = 30)  # Keyword arguments
# myfunc(b= 20, a = 10, c = 20)  # Keyword arguments
# myfunc(10, 20, c = 30)  # 10 20 30
# myfunc(10, b = 20, c = 30)  # 10 20 30
# myfunc(10, b = 20, 30)  # This is wrong as positional arguments must appear before any keyword arguments
# myfunc(10, 30, b=20)  # myfunc() got multiple values for argument 'b'

# Example 5: Function can return multiple values
def largest(a, b):
    if a > b:
        return a,b
    else:
        return b,a
print(largest(100, 200))  # (200, 100)
print(largest(20, 10))
res = largest(10, 20)
print(res)
print(type(res))