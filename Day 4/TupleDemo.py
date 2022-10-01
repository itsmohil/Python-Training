# Example 1 creating tuple
# myTuple = ("apple", "banana", "cherry")
# print(myTuple)
# myTuple = ()  # Empty tuple

# Example 2 Access tuple items
# myTuple = ("apple", "banana", "cherry")
# print(myTuple[1])  # Banana

# Example 3 range of indexes
# myTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(myTuple[2:5])  # ('cherry', 'orange', 'kiwi')
# print(myTuple[-4:-1])  # ('orange', 'kiwi', 'melon')

# Example 4 Changing tuples value
# by default tuple does not allow you change value because it is immutable
# myTuple = ("apple", "banana", "cherry", 10, "kiwi", "melon", "mango")
# myList = list(myTuple)
# myList[0] = "grapes"
# myTuple = tuple(myList)
# print(myTuple)

# Example 5 reading tuple items using loop
# myTuple = ("apple", "banana", "cherry")
# for i in myTuple:
#     print(i)

# Example 6 Check if item exists in tuple
# myTuple = ("apple", "banana", "cherry")
# if "banana" in myTuple:
#     print("Exists in tuple")
# else:
#     print("Not in tuple")

# Example 7 find total number items in tuple
# myTuple = ("apple", "banana", "cherry")
# print(len(myTuple)

# Example 8 Add items in the tuple - not possible because tuples are immutable
# myTuple = ("apple", "banana", "cherry")
# Not possible

# Example 9 copy tuple
# myTuple1 = ("apple", "banana", "cherry")
# myTuple2 = myTuple1
# print(myTuple2)

# Example 10 removing items - Not possible because tuple is immutable
# myTuple = ("apple", "banana", "cherry")
# del myTuple
# print(myTuple)  # NameError: name 'myTuple' is not defined. Did you mean: 'tuple'?

# Example 11 Join/combine tuple
# tuple1 = (10, 20, 30)
# tuple2 = ("a", "b", "c")
# tuple3 = tuple2 + tuple1
# print(tuple3)

# Example 12 compare tuple1 = tuple2
tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)
if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")