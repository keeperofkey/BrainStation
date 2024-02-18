#!/usr/bin/python3
print("Hello World!")
users = []
users.append("Wendy")
users.append("Kevin")
users.append("Frank")
users.append("Alicia")
users.append("Riley")
print("Original List: ", users)
users.sort()
print("Sorted List: ", users)
users.sort(reverse=True)
print("Reversed List: ", users)
users.pop(2)
print("Updated List: ", users)

medict = {'name': 'liam', 'age': '28'}
print("MyDict: ", medict)
hobbies = []
medict['hobbies'] = hobbies
hobbies.append("Skiing")
hobbies.append("Gaming")
hobbies.append("Keyboards")
print("MyDict: ", medict)
