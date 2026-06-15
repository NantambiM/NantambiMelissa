def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

def modulus(a, b):
    return a % b

def numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def menu():
    print("Welcome to my calculator")

    print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
""")

    return int(input("Enter your choice: "))

def calculate(choice, a, b):
    match choice:
        case 1:
            soln = addition(a, b)
        case 2:
            soln = subtraction(a, b)
        case 3:
            soln = multiplication(a, b)
        case 4:
            soln = division(a, b)
        case 5:
            soln = modulus(a, b)
        case _:
            print("Invalid choice")
            return

    print(f"Solution is: {soln}")

choice = menu()
a, b = numbers()
calculate(choice, a, b)