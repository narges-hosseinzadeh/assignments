set_user="narges"
set_password="1234"

c = 0
loop = 0
while loop < 3 :
    loop += 1
    user=input("please enter your user")
    password=input("please enter your password")
    if (user==set_user) and (password==set_password):
        print('wellcome')
        break
    else:
        c += 1
        if (c < 3):
            print('wrong username or password!try again!')
            continue
        elif (c == 3):
           print('your account has been locked')
        

        
    

