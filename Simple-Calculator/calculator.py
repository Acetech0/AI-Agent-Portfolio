def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x % y

def main():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation: 1) Add 2) Subtract 3) Multiply 4) Divide 5) Power 6) Modulo")
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")
    elif choice == "5":
        print(f"Result: {power(num1, num2)}")
    elif choice == "6":
        print(f"Result: {modulo(num1, num2)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()