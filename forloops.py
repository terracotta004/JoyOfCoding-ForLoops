# forloops.py
# Ben Underwood

for i in range(1,6):
    print(i)

print()

for j in range(2, 12, 3):
    print(j)

print()

for k in range(-10, 1, 2):
    print(k, end=" ")

print("\n")

# Method 1 for printing a 4x4 square of asterisks:

# for l in range(4):
#     print("****")

# print()

# Method 2 for printing a 4x4 square of asterisks:

# for l in range(4):
#     print("*" * 4)

# print()

# Method 3 for printing a 4x4 square of asterisks:

for l in range(4):
    for m in range(4):
        print("*", end="")
    print()

print()

for char in "CSCI 150":
    print(char)

print()

for num in range(1, 11):
    print(num)

