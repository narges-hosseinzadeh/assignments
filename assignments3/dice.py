sum=0
while True:
    
    dice=int(input('roll the dice'))
    sum=sum+dice
    if dice==6:
        break
    if dice<6: 
        continue
        
print("the sum of rolled dices is" , sum)