number1 = input('Enter the num:')
num1 = float(number1)
sign = input('Enter the sign(+,-,*,/):')
number2 = input('Enter the num:')
num2 = float(number2)
if sign == '+':
    print('your result is '+ str(num1+num2))
elif sign == '-':
    print('your result is '+ str(num1-num2))
elif sign == '*':
    print('your result is '+ str(num1*num2))
elif sign == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print('Your result is: ' + str(num1 / num2))
else:
    print('Please enter +,-,* or /')
