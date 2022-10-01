# Example 1 Creating Dictionary
# myDic = {101: "x", 102: "y", 103: "z"}
# print(myDic)  # {101: 'x', 102: 'y', 103: 'z'}

# Example 2 Access the values from the key
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# print(myDic["brand"])  # Hyundai
# print(myDic["model"])  # i10
# # Using get function
# x = myDic.get("brand")  # Hyundai
# print(x)

# Example 3 Change values in the dictionry
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# myDic["year"] = 2022
# print(myDic.get("year"))

# Example 4 Reading items from dictionary using loop
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# for i in myDic:
#     print(i)  # only print keys from Dictionary
#
# for i in myDic:
#     print(myDic[i])  # only prints values from Dictionary
#
# for i in myDic.values():
#     print(i)  # only prints values from Dictionary

# for x,y in myDic.items():
#     print(x, ":", y)  # prints keys along with the values

# Example 5 Check key exists in the value
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# if "model" in myDic:
#     print("Exists")
# else:
#     print("Does not exists")

# print("model" in myDic)

# Example 6 Find number of items in dictionary
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# print(len(myDic))

# Example 7 Adding items to dictionary
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# myDic["colour"] = "red"
# print(myDic)

# Example 8 Remove items from dictionary
# myDic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# myDic.pop("year")
# print(myDic)  # {'brand': 'Hyundai', 'model': 'i10'}
# del myDic["year"]
# print(myDic)  # {'brand': 'Hyundai', 'model': 'i10'}
# del myDic
# print(myDic)  # NameError: name 'myDic' is not defined
# myDic.clear()
# print(myDic)  # {}

# Example 9 Copying dictionary
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
# Without using copy method
# myDic2 = myDic
# print(myDic2)

# Using Copy method
myDic2 = myDic.copy()
print(myDic2)