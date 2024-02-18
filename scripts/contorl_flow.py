#!/usr/bin/python3
print('hello world!')

# EXERCISE 1
arr = [2, 10, 5, 8, 7]
for i in arr:
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

# EXERCISE 2
students = [
    {
        "name": "Alan",
        "grade": 90
    },
    {
        "name": "Steve",
        "grade": 52
    },
    {
        "name": "Jessica",
        "grade": 87
    }
]
for i in students:
    print("name: ", i["name"], "\ngrade: ", i["grade"])

# EXERCISE 3
count = 1
even = 0
odd = 0
while count <= 10:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    count += 1
print("Num of Even: ", even, "\nNum of Odd: ", odd)

# EXERCISE 4
for i in range(1, 11):
    print(i)

# EXERCISE 5
names = ["Alice", "Bob", "Charlie"]
for i in names:
    print((i + "\n") * 4 + i)
