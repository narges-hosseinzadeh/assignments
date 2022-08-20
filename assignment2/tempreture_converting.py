choice = int(input('for converting  °F to °C press 1'
  'for converting  °C to °F press 2'
  'for converting  °C to °K press 3' 
  'for converting  °K to °C press 4'
  'for converting  °K to °F press 5' 
  'and for converting  °F to °K press 6 '))
t = float(input('enter tempreture = '))
if choice == 1:
    C = 5/9*(t- 32)
    print('the temperature is' , C , '°c')

elif choice == 2:
    F = 9/5*t + 32
    print('the temperature is' , F , '°F')

elif choice == 3:
    K = t + 273
    print('the temperature is' , K , '°K')

elif choice == 4:
    C = t- 273
    print('the temperature is' , C , '°c')

elif choice == 5:
    F = 9/5*(t - 273) + 32 
    print('the temperature is' , F , '°F')

elif choice == 6:
    K = 5/9*(t - 32) + 273
    print('the temperature is' , K , '°K')
