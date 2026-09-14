def valid_login(username, password):
    """Return whether the credentials match the stored account."""
    return username == "admin" and password == "python123"


def login(max_attempts=3):
    """Allow a limited number of login attempts."""
    for _ in range(max_attempts):
        if valid_login(input("Username: "), input("Password: ")):
            return True
        print("Invalid credentials")
    return False


def session():
    """Run the authenticated session until logout."""
    while True:
        choice = input("1. Profile  2. Logout: ")
        if choice == "1":
            print("Welcome, admin")
        elif choice == "2":
            return
        else:
            print("Invalid choice")


def main():
    """Control authentication and logout."""
    while login():
        session()
        if input("Try again? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()
