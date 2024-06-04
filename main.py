# Function to display the menu
def display_menu():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == "2":
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result of division: {result}")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
