# # Example 1 how to create a list
# myList1 = [10, 20, 30, 40, 50]
# myList2 = ["Apple", "Banana", "Cherry"]
# myList3 = ["Apple", 10, "Banana", 20]
# myList = []
#
# print(myList1)
# print(myList2)
# print(myList3)
# print(myList)
#
# Example 2 Accessing items from the list
# myList = ["Apple", "Banana", "Cherry"] # index starts wih 0
# print(myList[1])  # Banana
# print(myList[-1])  # Cherry
#
# Example 3 Range of indexes
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# print(mylist[1:3])  # ['banana', 'cherry']
# print(mylist[-4:-1])  # ['orange', 'kiwi', 'melon']
#
# Example 4 change item value
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist)  # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# mylist[0] = "Mango"
# print(mylist)  # ['Mango', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
#
# Example 5 read list items using loop
# mylist = ["apple", "banana", "cherry"]
# for i in mylist:
#     print(i)
#
# Example 6 check if the item exist in list
# mylist = ["apple", "banana", "cherry"]
# if input("Enter str: ") in mylist:
#     print("Exists in the list")
# else:
#     print("It does not exist in the list")
#
# Example 7 List length counting number of items in the list
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))  # 3
#
# Example 8 Add new item in the list append() and insert()
# mylist = ["apple", "banana", "cherry"]
# print(mylist)  # ['apple', 'banana', 'cherry']
# mylist.append("orange")
# print(mylist)  # ['apple', 'banana', 'cherry', 'orange']
# mylist.insert(2, "melon")
# print(mylist)  # ['apple', 'banana', 'melon', 'cherry', 'orange']
#
# Example 9 Remove item from list pop() del()
# pop()
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)  # need to specify index of you want to remove
# print(mylist)
# del
# mylist = ["apple", "banana", "cherry"]
# del mylist[2]
# print(mylist)
# clear()
# mylist = ["apple", "banana", "cherry"]
# mylist.clear()
# print(mylist)
#
# Example 10 copy list
# Approach 1 list()
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = list(mylist1)
# print(mylist2)
#
# Approach 2 copy()
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = mylist1.copy()
# print(mylist2)
#
# Example 11 combine and join lists
# using + operators
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)  # ['a', 'b', 'c', 1, 2, 3]
#
# Using loop statement
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for i in list2:
#     list1.append(i)
# print(list1)
#
# # using extend()
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]
#
#
# Example 12 comparing lists
# list1 = [1, 2, 3.0]
# list2 = [1, 2, 3]
# if list1 == list2:
#     print("lists are equal")
# else:
#     print("lists are not equal")