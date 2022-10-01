# Create a String Variable

# s = "Welcome"
# s = str("welcome")

# Creation of empty string variables
# name = ""

# Mutable - Can change the value of variable
# Immutable - Cannot change the value of the variable
# String is immutable

# str1 = "Welcome"
# print(id(str1))  # 1481863772592
#
# str1 = str1 + " to Python"
# print(id(str1))  # 1481863826208

# if the value is changed after update then it is mutable

# Example3:+and with string
# str="welcome"
# print(str+"programming")#concatenation/joining
# print(str*3)  # welcomewelcomewelcome

# Example 4 Slicing []
# starting index 0
# ending index 1
# str1 = "Welcome"
# print(str1[1:3])  # el
# print(str1[:6])  # Welcom
# print(str1[2:])  # lcome
#
# print(str1[1:-1])  #elcom  Last char removed
# print(str1[1:-2])  #elco last 2 char removed

# Example 5 ord() and chr()
# print(ord("A"))  # 65 returns the ASCII code of the char
# print(chr(65))  # A returns char represented by ASCII number

# Example 6 min() max() len()
# print(min("abc"))
# print(max("abc"))
# print(len("abc"))

# Example 7 in not in operators
# s = "welcome"
# print("co" in s)  # True
# print("lome" in s)  # False
# print("wel" not in s)  # False
# print("mel" not in s)  # False

# Example 8 : String Comparison
# print("tim"=="tie")  # False
# print("free"!="freedom")  # True
# print("arrow">"aron")  # True
# print("right">="left")  # True
# print("teeth"<"tee")  # False
# print("yellow"<="fellow")  # False
# print("abc">"")  # True

# Example 9 testing strings True/False
# s = "welcome to python"
#
# print(s.isalnum())  # False
# print("welcome".isalpha())  # True
# print("2012".isdigit())  # True
# print("first number".isidentifier())  # False
# print(s.islower())  # True
# print("WELCOME".isupper())  # True
# print(" ".isspace())  # True

# Example 10 searching for substrings
# s = "welcome to python"
# print(s.endswith("thon"))  # True
# print(s.startswith("good"))  # False
# print(s.find("come"))  # 3
# print(s.find("become"))  # -1 not found
# print(s.count("t"))  # 2 # Returns number of occurrence of substring of the string


# Example 11 converting strings
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)  # String in python
# s2 = s.title()
# print(s2)  # String In Python
# s3 = s.lower()
# print(s3)  # string in python
# s4 = s.upper()
# print(s4)  # STRING IN PYTHON
# s5 = s.swapcase()
# print(s5)  # sTRING IN python
# s6 = s.replace("in", "on")
# print(s6)  # Strong on PYTHON

# Example 12 reverse string
# Method 1
# s = "Welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str
# print("reversed string is:",rev_str)  # emocleW

# Method 2
s = "welcome"
rev_str = s[::-1]
print(rev_str)


