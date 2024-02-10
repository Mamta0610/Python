Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hi")
Hi
num1 = 55
num2= 66
print("Add is ", num1+num2)
Add is  121
num1=input("Enter number ")
Enter number 66
num2 = input("Enter number ")
Enter number 55
print(num1+num2)
6655
num1=float(input("Enter number "))
Enter number 55.6
num2=int(input("Enter number "))
Enter number 66.10
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    num2=int(input("Enter number "))
ValueError: invalid literal for int() with base 10: '66.10'
ValueError: invalid literal for int() with base 10: '66.10'Enter number 66.10num2=int(input("Enter number "))
SyntaxError: invalid decimal literal
num2=int(input("Enter number "))
Enter number 12
print(num1+num2)
67.6
name = str(input("Enter name "))
Enter name mamta
print("My name is ", + name)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("My name is ", + name)
TypeError: bad operand type for unary +: 'str'
print("My name is ", name)
My name is  mamta
num1 = 10
num1+=20
print(num1)
30
num1++
SyntaxError: incomplete input
num1+=1
print(num1)
31
num1*=20
print(num1)
620
x = int(input("Enter number "))
Enter number 45
y = int(input("Enter second number "))
Enter second number 66
if(x>y):
       print("Number is greater ")
else:
       print("number is not greater")

number is not greater
if(x>y):
       print("Number is greater ")
       else:
              
SyntaxError: invalid syntax
percentage= float(input("Enter percentage "))
Enter percentage 55
if percentage>=80 :
       print(" O grade ")
else:
       if percentage>=70
       
SyntaxError: incomplete input
else:
       
SyntaxError: invalid syntax
if percentage>=80 :
       print("O grade")
elif(percentage>=70):
       print(" A grade ")
elif(percentage>=60):
       print("B grade ")
elif(percentage>=50):
       print("C grade ")
elif(percentage>=40):
       print("D grade ")
else:
...        print(" Fail ")
... 
C grade 
>>> name = "itvedant"
>>> print ('it' in name)
True
>>> print ('tt' in name)
False
>>> print ('it' not in name)
False
>>> print ('tt' not in name)
True
>>> x =10
>>> y=10
>>> print(id(x))
140708870218824
>>> print(id(y))
140708870218824
>>> print(x is y)
True
>>> print(x is not y)
False
