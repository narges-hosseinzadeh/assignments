clock_converter = int(input('for converting hour to second press 1 and for converting second to hour press 2 '))
if (clock_converter==1):
    hour=int(input('insert the hour'))
    min=int(input('insert the minute'))
    sec=int(input('insert the second'))
    sec1=hour*3600
    sec2=min*60
    second=sec1+sec2+sec
    print( 'the clock is', second,'second')
elif (clock_converter==2):
    second=int(input('insert the clock in second'))
    hour = second // 3600
    min1 = second % 3600
    min = min1 // 60
    sec = min1 % 60

    print ('the clock is :',hour,':', min,':', sec) 
