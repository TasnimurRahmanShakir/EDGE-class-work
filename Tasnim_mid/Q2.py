var = input('Enter a value: ')
if var.isdigit():
    print('value is Digit')
elif var.isalpha():
    print('Value is string')
else:
    print('Special character')