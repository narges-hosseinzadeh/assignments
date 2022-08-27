import math
times=int(input('how many times do you want to use calculator'))
calculator_type=int(input('for basic calculator type 1 and for advanced calculator type 2 '))
c=0
while c<times:
   print('you have tried', c, "times")
   c+=1
   if (calculator_type==1):
      operation=input('enter your desired operation by choosing + , - , * , /,')
      num1=float(input('insert the first number'))
      num2=float(input('insert the second number'))
      if (operation == "+"): 
         print(num1, "+", num2, "=", (num1 + num2))      
      elif (operation == "-"): 
         print(num1, "-", num2, "=", (num1 - num2))  
      elif (operation == "*"): 
         print(num1, "*", num2, "=", (num1 * num2))  
      elif (operation == "/"): 
         if (num2!=0):
            print(num1, "/", num2, "=", (num1 / num2))   
         elif(num2==0):
            print ('the devision is undefined')
      else:
            print('the operation is undefined in basic calculator you should use the advanved mode!')

   elif (calculator_type==2):
      operation=input('enter your desired operation by choosing + , - , * , % , || , ^, / , //,sin , cos, tan, cot ')
      if(operation=='+' or operation=='-' or operation=='*' or operation=='%' or operation=='/' or operation=='//' or operation=='^'):
         num1=float(input('insert the first number'))
         num2=float(input('insert the second number'))
         if (operation == "+"): 
             print(num1, "+", num2, "=", (num1 + num2))        
         elif (operation == "-"): 
             print(num1, "-", num2, "=", (num1 - num2))
         elif (operation == "*"): 
             print(num1, "*", num2, "=", (num1 * num2))
         elif (operation == "/"): 
            if (num2!=0):
               print(num1, "/", num2, "=", (num1 / num2))
            elif(num2==0):
               print ('de devision is undefined')
         elif (operation == "%"): 
            print(num1, "%", num2, "=", (num1 % num2))
         elif (operation == "//"): 
            print(num1, "//", num2, "=", (num1 // num2))
         elif (operation == "^"): 
            print(num1, "^", num2, "=", (num1 ** num2))
      elif(operation=='||' or operation=='sin' or operation=='cos' or operation=='tan' or operation=='cot'):
         num=float(input('insert the number'))
         if (operation == "||"): 
            print('|',num,'|', "=", abs(num))
         elif(operation=='sin'):
            print('sin(',num,')', "=", math.sin(num))
         elif(operation=='cos'):
            print('cos(',num,')', "=", math.cos(num))
         elif(operation=='tan'):
            print('tan(',num,')', "=", math.tan(num))
         elif(operation=='cot'):
            print('cot(',num,')', "=", math.cot(num))
      else:
         print('undefined operation')