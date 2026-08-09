    
while True:
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        divide = first_number / second_number
        print(divide)
        break
    # ValueError shows when user inputs anything but a number. ZeroDivisionError shows when user tries to divide first number by 0
    except (ValueError, ZeroDivisionError):   
        pass