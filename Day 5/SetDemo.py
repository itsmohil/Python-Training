# Example 1 Creating set
# mySet = {"apple", "banana", "cherry"}
# print(mySet)

# Example 2 Accessing items from set
# mySet = {"apple", "banana", "cherry"}
# for i in mySet:
#     print(i)

# Example 3 Value exist in set or not
# mySet = {"apple", "banana", "cherry"}
# print("banana" in mySet)  # True
# print("banana2" in mySet)  # False

# Example 4 adding items to set
# Add()-Add single item   update()-add multiple item
# mySet = {"apple", "banana", "cherry"}
# # mySet.add("orange")
# # print(mySet)  # {'cherry', 'apple', 'orange', 'banana'}
# # mySet.update(["kiwi", "mango"])
# # print(mySet)  # {'cherry', 'mango', 'apple', 'orange', 'banana', 'kiwi'}

# Example 5 Length of set
# mySet = {"apple", "banana", "cherry"}
# print(len(mySet))  # 3

# Example 6 removing a item - remove()  discard()
# mySet = {"apple", "banana", "cherry"}
# mySet.remove("apple")
# # mySet.remove("xyz")  # KeyError because of item does not exist
# mySet.discard("banana")
# mySet.discard("xyz")  # Will not show any error
# print(mySet)

# Example 7 Clear all item from set
# mySet = {"apple", "banana", "cherry"}
# mySet.clear()
# print(mySet)  # set()
# del mySet
# print(mySet)  # NameError: name 'mySet' is not defined

# Example 8 Joining 2 - union()   update()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
