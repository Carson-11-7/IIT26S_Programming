print('Program starting.')
name=input('What is your name: ')
num1=float(input('Enter a floating point number: '))
num2=float(input('Enter second floating point number: '))
print(f'{name} you gave nunbers {num1} and {num2}')
product=num1*num2
rounded_product = round(product, 2)
print(f'Multiplying first and second number will result in product {rounded_product}')
print('Program ending.')
