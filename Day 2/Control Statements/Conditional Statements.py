# conditional statements
#         if,  if..else,  elif


# Example 1: Print a person is eligible for Vote or Not
# age>=18

# age = int(input("Enter Age:"))

# if age >= 18:
#     print("eligible for vote")
# else:
#     print("Not Eligible for Vote")

# Example 2

# if True:
#     print("True condition")
# else:
#     print("False condition")

# Example 3

# if 1:
#     print("One")
# else:
#     print("Two")


# Example 4 Find a number is odd/even num%2=0

# num = 15

# if num%2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# Example 5 if  else in a single line (ternary operator )
#
# num = 10
#
# print("Even Number") if num%2==0 else print("Odd Number")

# Example 6 if else - multiple statements in single line
# a = 5
#
# {print("Hello"), print("python")} if a>10 else {print("Hi"), print("Java")}

# Example 7 Muliple conditions using elif

# weekno = 10
#
# if weekno == 1:
#     print("Sunday")
# elif weekno == 2:
#     print("Monday")
# elif weekno == 3:
#     print("Tuesday")
# elif weekno == 4:
#     print("Wednesday")
# elif weekno == 5:
#     print("Thursday")
# else:
#     print("Invalid Week Number")



# Assignments
# 1) Check the given number is Positive or negative
# 2)Check the largest of 2numbers
# 3)Check the largest of 3numbers
# 4)Print week number if you provide weekname as input.

# 1) a = 0
#
# if a >= 0:
#     print("Number is Positive")
# else:
#     print("Number is Negative")

# 2)

# a = 10
# b = 5
#
# if a > b:
#     print("a is bigger than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("b is bigger than a")

# 3)
# a = 9
# b = 4
# c = 3
#
# if a>b and a>c:
#     print("A is the largest")
# elif b>a and b>c:
#     print("B is the largest")
# else:
#     print("C is the largest")

# 4)

weekday = "Monday"

if weekday == "Sunday":
    print("1")
elif weekday == "Monday":
    print("2")
elif weekday == "Tuesday":
    print("3")
elif weekday == "Wednesday":
    print("4")
elif weekday == "Thursday":
    print("5")
else:
    print("Invalid Weekday")