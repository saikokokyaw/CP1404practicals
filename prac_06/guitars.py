"""
languages
Estimate: 20 minutes
Actual: 30 minutes
"""


from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)

        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"

            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()