Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #take a sample string
>>> info="LearnProgram"
>>> if info=="Learn"
SyntaxError: incomplete input
>>> if info="Learn" :
...     
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> if info=="Learn" :
...     print("good Morning ")
... elif info=="Program" :
...     print("good afternoon ")
... elif info=="Learning" :
...     print("good evening ")
... elif info=="LearnProgram" :
...     print("I am learning python")
... else:
...     print("Invalid ")
... 
I am learning python
