number = int(input("Enter Number : "))
if number % 7 == 0:
    print('The number is a multiple of 7')
else:
    new_number = number + (7 - number % 7)
    print('the inserted number is not multiple of 7,The next number which is a multiple of 7 =', new_number)