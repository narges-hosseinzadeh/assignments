
set_password="1234"
reversed_password="4321"
c = 0
while True :
    password=input("please enter your password")
    if (len(password)<4) or (len(password)>4):
       print('the lenght of password is not correct! try again')
       continue
    if (password==set_password):
        print('correct password')
        break
    elif (password==reversed_password):
        print('we called the police')
        break
    else:
        c += 1
        if (c < 3):
            print('wrong password! try again!')
            continue
        elif (c == 3):
           print('your account has been locked')
           break
        

        
    

