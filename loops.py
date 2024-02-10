Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#print table using for loop
num=int(input("Enter number for table "))
Enter number for table 6
for i in range(1,11):
    print("value : ", num*i)

value :  6
value :  12
value :  18
value :  24
value :  30
value :  36
value :  42
value :  48
value :  54
value :  60
for i in range(1,11,2):
    print("value : ", num*i)

value :  6
value :  18
value :  30
value :  42
value :  54
value :  54
for i in range(1,11,1):
    print(i)

1
2
3
4
5
6
7
8
9
10
>>> i=1
>>> while(i<11):
...     print(num*i)
...     i =i+1
... 
6
12
18
24
30
36
42
48
54
60
