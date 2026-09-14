def calculator(first, operator, second):
    """Return a calculator result or an error message."""
    if operator == "+": return first + second
    if operator == "-": return first - second
    if operator == "*": return first * second
    if operator == "/": return "Cannot divide by zero" if second == 0 else first / second
    return "Invalid operator"


def palindrome(text):
    """Return whether text reads the same forwards and backwards."""
    return text == text[::-1]


def is_prime(number):
    """Return whether a number is prime."""
    if number < 2: return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0: return False
    return True


def factorial(number):
    """Return a non-negative integer's factorial."""
    if number < 0: return "Number must be non-negative"
    result = 1
    for value in range(2, number + 1): result *= value
    return result


def main():
    """Run the utility menu."""
    while True:
        print("1. Calculator  2. Palindrome  3. Prime  4. Factorial  5. Exit")
        choice = input("Choose: ")
        if choice == "5": break
        if choice == "1": print(calculator(float(input()), input("Operator: "), float(input())))
        elif choice == "2": print(palindrome(input("Text: ")))
        elif choice == "3": print(is_prime(int(input("Number: "))))
        elif choice == "4": print(factorial(int(input("Number: "))))
        else: print("Invalid choice")


if __name__ == "__main__":
    main()
