"""
CP1404/CP5632 - Practical
Sales bonus program
"""

total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input(f"Price of item {i+1} : "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print("Total price for ", number, " items is $", total, sep='')

# with string formatting for currency output
print("Total price for {} items is ${:.2f}".format(number, total))