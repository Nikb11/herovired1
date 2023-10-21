import re

def check_password_strength(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_character = "!@#$%^&*()_-+={}[]|\:;\"'<>,.?/~"
    if not any(char in special_character for char in password):
        return False

    return True

def main():
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Password is strong and meets all criteria.")
    else:   
        print("Password is weak and does not meet the criteria.")

if __name__ == "__main__":
    main()
