
num1 = float(input("Enter a first number:"))
num2 = float(input("Enter a second number:"))

print("Enter 1 for 'Addition'\nEnter 2 for 'Subtraction'\nEnter 3 for 'Multiplication'\nEnter 4 for 'Division'")

Enter_number = int(input("choice a number from 1-4:"))


if Enter_number == 1:
    print("Addition for your first and second number is :",num1+num2)

elif Enter_number == 2:
    print("subtraction for your first and second number is :",num1-num2)

elif Enter_number == 3:
    print("Multiplication for your first and second number is :",num1*num2)

elif Enter_number == 4:
    print("Division for your first and second number is :",num1/num2)

else:
    print("Please enter a valid choice:")
