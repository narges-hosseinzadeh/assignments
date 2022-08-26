number=25
c=0
while True:
    system_guess=int(input('guess a number'))
    c+=1
    if system_guess>number:
        print('your number is bigger')
    elif system_guess<number:
        print('your number is lower')
    else:
        print('Well done')
        break
print('you tries',c,'times')
