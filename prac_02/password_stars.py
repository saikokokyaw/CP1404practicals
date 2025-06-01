"""
CP1404 - Practical 
Get a password with minimum length and display asterisks
"""
def main():
    password = get_password()
    print("*"* len(password))


def get_password():
    password = input("Enter password:")
    while len(password) <= 3:
        print("Invalid")
        password = input("Enter password:")
    return password
main()