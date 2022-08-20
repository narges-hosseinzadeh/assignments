number = int(input('enter the number'))
if number==0:
    print('The inverse of zero is undefined')
else:
    reversed_number=1/number
    if number==reversed_number:
        print('The inserted number is equal to its inverse')
    elif number!=reversed_number:
        print('The inserted number is not equal to its inverse')