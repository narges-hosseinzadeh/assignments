height = float(input('enter your height in m'))
weight = float(input('enter your weight in Kg'))
BMI = weight/(height*height)
if BMI < 18.5:
    print('your BMI is =',BMI,',You are underweight')
elif 18.5 <= BMI <= 24.9:
    print('your BMI is =',BMI,',You are at a healthy weight')
elif 25 <= BMI <= 29.9:
    print('your BMI is =',BMI,',You are overweight')
elif 30 <= BMI <= 39.9:
    print('your BMI is =',BMI,',You are obese')