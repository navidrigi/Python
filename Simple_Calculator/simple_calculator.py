'''
This is a simple calculator that asks user for numbers
and calculates the result.
'''

def main():
    input_validation()

def input_validation():
    while True:
        try:
            num1 = int(input('Enter your 1st number: '))
            break
        except ValueError:
            print('Please enter a valid number')
    while True:
        try:
            num2 = int(input('Enter your 2nd number: '))
            break
        except ValueError:
            print('Please enter a valid number')
    while True:
        ops = ['+', '-', '*', '/', '//', '%', '**']
        op = ""
        while op not in ops:
            op = input("Enter your operator('+', '-', '*', '/', '//', '%', '**'): ")
        break
    calculations(num1, num2, op)
    if input('Continue? ').lower() == 'no':
        exit()
    input_validation()

def calculations(num1, num2, op):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '//':
        print(num1 // num2)
    elif op == '%':
        print(num1 % num2)
    elif op == '**':
        print(num1 ** num2)

main()
