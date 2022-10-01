# Example 1
# global_var = 20
#
# def func():
#     local_var = 10
#     print(local_var)
#     print(global_var)

# func()

# print(local_var)  # Invalid because local_var is local variable to the func()
# print(global_var)  # Valid because global_var is global variable

# Example 2
# xy = 100  # Global Variable
# def cool():
#     xy = 200
#     print(xy, "Local")  # Local Variable
# cool()

# Example 3
# xy = 100  # Global Variable
# def cool():
# #   global xy = 20  # Invalid Syntax
#     global xy
#     xy = 200
#     print(xy, "Local")  # Local Variable
# cool()  # 200 Local
# print(xy)  # 200

# Example 4
# x = 100
# def cool():
#     global x
#     x = 500
#     print(x)
# # cool()
# print(x)

# Example 5
def cool():
    global x
    x = 100
    print(x)
print(x)  # Syntax Error
cool()  # 100
print(x)  # 100