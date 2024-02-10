Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
price=500
quantity=1
amount = quantity * price
if(amount>200):
    print("Hi")

Hi
if(amount>200) :
    if(amount>1000) :
        print("Hi ")
    else:
        if(amount<=1000 and amount>600):
            print("hello")
        elif(amount<=600 and amount>400) :
            print("good")
        else:
            print("200-400")
    elif(amount==200):
        
SyntaxError: invalid syntax
if(amount>200) :
    if(amount>1000) :
        print("Hi")
    else:
        if(amount<=1000 and amount>600):
            print("hello")
        elif(amount<=600 and amount>400):
            print("good")
        else:
            print("200-400")
        elif(amount==200):
            
SyntaxError: invalid syntax
if(amount>200) :
    if(amount>1000) :
        print("Hi ")
    else:
        if(amount<=1000 and amount>600):
            print("hello")
        elif(amount<=600 and amount>400) :
            print("good")
        else:
            print("200-400")
    elif(amount==200):
        
SyntaxError: invalid syntax
if(amount>200) :
    if(amount>1000) :
        print("Hi ")
    else:
        if(amount<=1000 and amount>600):
            print("hello")
        elif(amount<=600 and amount>400) :
            print("good")
        else:
            print("200-400")
    elif(amount==200):
...         
SyntaxError: invalid syntax
>>> if(amount>200) :
...     print("Hi ")
... 
Hi 
>>> if(amount>200) :
...     if(amount>1000) :
...         print("Hi ")
...     else:
...         if(amount<=1000 and amount>600):
...             print("Hello")
...         elif(amount<=600 and amount>400):
...             print("good")
...         else:
...             print("200-400")
... elif(amount==200):
...     print("Amount is 200")
... else:
...     print("amount less than 200 ")
... 
good
