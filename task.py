
def main():
    print("--- Python Mini Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operation = input("Choose operation (+, -, *, /): ").strip()
        if operation == '+':
            result = num1 + num2
            print(f"Result: {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {result}")
            
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        
        else:
            print("Invalid operation! Please run the program again and choose +, -, *, or /.")

    except ValueError:
         print("Invalid input! Please enter numeric values only.")

if name == "__main__":
    main()