"""
CP1404/CP5632 - Practical
Loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()


n = int(input("Number of stars: "))

# Print n stars on one line
for i in range(n):
    print("*", end="")

print()


n = int(input("Enter a number: "))

stars = ""
for i in range(n):
    stars += "*"
    print(stars)