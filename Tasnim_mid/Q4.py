num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

relation = ''

if num1 > num2:
    relation += 'num1 is greater than num2\n'
if num1 < num2:
    relation += 'num1 is less than num2\n'

if num1==num2:
    relation += 'num1 is equal to num2\n'
else:
    relation += 'num1 is not equal to num2\n'

if num1<=num2:
    relation += 'num1 is less than or equal num2\n'
else:
    relation += 'num1 is greater than or equal num2\n'
    
print(relation)