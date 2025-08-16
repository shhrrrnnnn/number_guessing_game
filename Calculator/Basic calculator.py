import math
while True:
    print("What operation do you want to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (a^b)")
    print("6. Modulus (a % b)")
    print("7. Square root")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("The sum is:", a + b)

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("The difference is:", a - b)

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("The product is:", a * b)

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("The division result is:", a / b)

    elif choice == '5':
        a = float(input("Enter base number: "))
        b = float(input("Enter exponent: "))
        print("The result of power is:", a ** b)

    elif choice == '6':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Cannot perform modulus with zero!")
        else:
            print("The modulus is:", a % b)

    elif choice == '7':
        a = float(input("Enter the number to find square root of: "))
        if a < 0:
            print("Error: Cannot find square root of negative number!")
        else:
            print("The square root is:", math.sqrt(a))

    elif choice == '8':
        print("Thank you for using the calculator. Goodbye!")
        break

    else:
        print("Invalid input. Please select a valid option.")
    
    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != 'y':
        print("Thank you for using the calculator. Goodbye!")
        break



    