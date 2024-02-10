Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#calculate leap year
year=int(input("Enter you to check "))
Enter you to check 2021
if (year%4==0) :
    if(year%100==0):
        if(year%400==0):
            print("Its leap year ")
        else:
            print("Its not a leap year ")
...         else:
...             
SyntaxError: invalid syntax
>>> if (year%4==0) :
...     if(year%100==0):
...        if(year%400==0):
...            print("Its leap year ")
...         else:
...             
SyntaxError: unindent does not match any outer indentation level
>>> if (year%4==0) :
...     if(year%100==0):
...         if(year%400==0):
...             print("Its a leap year ")
...         else:
...             print("its not leap year ")
...     else:
...         print("its an leap year ")
... else:
...     print("its not leap year ")
... 
its not leap year 
