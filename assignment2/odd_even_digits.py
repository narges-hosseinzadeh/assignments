numbers =int(input("enter the number"))
even_numbers = 0
odd_numbers = 0
while (numbers > 0):
    dig = numbers % 10
    numbers = numbers // 10 
    if dig % 2 == 0:
        even_numbers += 1
    elif dig % 2 != 0:
        odd_numbers += 1
#if numbers==0:
   # print("the number has been entered is zero")
if even_numbers > odd_numbers:
    print("even digits are more than odd digits")
elif even_numbers == odd_numbers:
    print("even digits are equal odd digits")
elif even_numbers < odd_numbers:
    print("odd digits are more than even digits")
