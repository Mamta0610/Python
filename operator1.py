Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> print("value of x before increment",x)
value of x before increment 10
>>> x+=1
>>> print("value of x after increment",x)
value of x after increment 11
>>> y -=2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    y -=2
NameError: name 'y' is not defined
>>> y=10
>>> y-=2
>>> print(y)
8
