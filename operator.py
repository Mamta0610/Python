Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1=28
num2=78
print("Addition is : ", num1+num2)
Addition is :  106
print("Addition is : ", num1-num2)
Addition is :  -50
print("Division is : ", num1/num2)
Division is :  0.358974358974359
num1+=1
print(num1)
29
#num1= num1+1
num2-=2
print(num2)
76
n1=input("Enter number ")
Enter number 106
n2= input("Enter second number ")
Enter second number 75
print("Result is : ", n1+n2)
Result is :  10675
#using input() for taking value from user
>>> name=input("Enter qualification ")
Enter qualification MCA
>>> print("Qualification is : " , qualification)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("Qualification is : " , qualification)
NameError: name 'qualification' is not defined
>>> print("Qualification is : " , name)
Qualification is :  MCA
>>> n1=int(input("Enter number "))
Enter number 30
>>> n2=int(input("Enter number "))
Enter number 45
>>> print(n1+n2)
75
>>> print(n1*n2)
1350
>>> print("Result is : ", (n1*n2))
Result is :  1350
>>> a=10
>>> b=20.5
>>> print("sum is " , (a+b))
sum is  30.5
>>> sum is  30.5
False
int sum = a+b
SyntaxError: invalid syntax
int result=a+b
SyntaxError: invalid syntax
sum=a+b
print(sum)
30.5
print(type(sum))
<class 'float'>
