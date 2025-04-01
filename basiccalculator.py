def calculator():
    # Get the input of the user
    num1= float(input("Enter first number "))
    num2= float(input("Enter second number "))
    operation= input("Enter operation(-, *, /, +): ")


    # Perform Calculation
    if operation == '+':
        result= num1 + num2
        print (f"{num1} + {num2} = {result}")
    elif operation == '-':
        result= num1 - num2
        print(f"{num1} - {num2}= {result}")
    elif operation == '*':
        result= num1 * num2
        print(f"{num1} * {num2}= {result}")
    elif operation == '/':
    if num2== 0:
    print("Erroe: Division by zero is not allowed")
    else:
    result= num1/num2
    print(f"{num1} / {num2}= {result}")
    else:
    print("Invalid operation. Please enter -, +, *, /.")

    calculator()