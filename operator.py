Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import keyword
reserved_keywords = keyword.kwlist
print(reserved_kewywords)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(reserved_kewywords)
NameError: name 'reserved_kewywords' is not defined. Did you mean: 'reserved_keywords'?
>>> print(reserved_keywords)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a = 28
>>> b = 30
>>> print('a+b = ' , a+b)
a+b =  58
>>> print('a-b = ' , a-b)
a-b =  -2
>>> print('a*b = ' , a*b)
a*b =  840
>>> print('a/b = ' , a/b)
a/b =  0.9333333333333333
>>> print('a%b = ' , a%b)
a%b =  28
>>> print('exponent = ' , a**b)
exponent =  25986090120790645892257018950637850957185024
>>> #assignment
>>> x=10
... print("value of x before increment",x)
... 
... x+=1#x=x+1
... print("value of x after increment",x)
... 
... y=10
... print("value of y before decrement",y)
... 
... y-=2
... print("value of y after decrement",y)
SyntaxError: multiple statements found while compiling a single statement
>>> x=10
... print("value of x before increment",x)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> num=10
... print("value of x before increment",num)
SyntaxError: multiple statements found while compiling a single statement
