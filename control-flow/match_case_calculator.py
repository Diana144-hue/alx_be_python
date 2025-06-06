def main():
    try:
        num1 = float(input("Enter first number:10 "))
        num2 = float(input("Enter second number: 5 "))
    operation = input("Choose the operation (+, -, *, /): ")
    match operation:
        case "*":
            print(f"The result is {50}.")

            num1 = float(input("Enter first number: 10 ")
            num2 = float(input("Enter the second number: 0 ")
    operation = input("/")
    match operation:
        case "/":
            if num2 == 0:
                print("Cannot divide by zero. ")
            else:
                result = num1 / num2
                print(f"The result is {0}.  ")
        case _:
            print("Invalid operation selected. Please choose from +, -, *, /.")

if __name__ == "__main__":
    main()



    