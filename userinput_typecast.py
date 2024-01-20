Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_name=input(" Enter your name :  ")
 Enter your name :  mamta
>>> print(user_name)
mamta
>>> marks=int(input("Enter your marks : "))
Enter your marks : 66
>>> print(marks,type(marks))
66 <class 'int'>
>>> marks=int(input("Enter your marks : "))
Enter your marks : 66
>>> marks2=int(input("Enter your marks : "))
Enter your marks : 88
>>> res = marks + marks2
>>> print(res)
154
>>> marks=int(input("Enter your marks : "))
Enter your marks : 77.8
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    marks=int(input("Enter your marks : "))
ValueError: invalid literal for int() with base 10: '77.8'
>>> marks=float(input("Enter your marks : "))
Enter your marks : 77.8
>>> print(marks)
77.8
