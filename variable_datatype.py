Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("variables examples")
variables examples
>>> num = 14
>>> print(type(num))
<class 'int'>
>>> name ="mamta"
>>> print(type(name))
<class 'str'>
>>> num=123.45
>>> print(type(num))
<class 'float'>
>>> status=true
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> status=True
>>> print(type(status))
<class 'bool'>
>>> gender=m
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    gender=m
NameError: name 'm' is not defined
>>> gender="M"
>>> print(type(gender))
<class 'str'>
>>> a=60
>>> b=a
>>> print(b)
60
>>> //type is inbuilt function to check datatype of variable
SyntaxError: invalid syntax
>>> xx =614
>>> print("Value of xx : " , xx)
Value of xx :  614
