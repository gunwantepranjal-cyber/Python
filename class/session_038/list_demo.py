Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> L =[10,20,30]
>>> M = L * 5
>>> print(L)
[10, 20, 30]
>>> print(M)
[10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]
>>> L+L+L+L+L+L
[10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]
>>> L * 1.5
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    L * 1.5
TypeError: can't multiply sequence by non-int of type 'float'
>>> L * 0
[]
>>> l * 1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l * 1
NameError: name 'l' is not defined. Did you mean: 'L'?
>>> L * 1
[10, 20, 30]
>>> L * 2
[10, 20, 30, 10, 20, 30]
>>> L * 3
[10, 20, 30, 10, 20, 30, 10, 20, 30]
>>>  s = '-'
...  
SyntaxError: unexpected indent
>>> s = ' - '
>>> line = s * 80
>>> print(line)
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 
>>> #memebership testing operator
...  
>>> L = [10,20,30,40]
>>> 10 in L
True
>>> 20 in L
True
>>> 30 in L
True
40 in L
True
50 in L
False
60 in L
False
False in :
    
SyntaxError: invalid syntax
#step 4 : class Methods
#append() function : To all one object built - in or container at the end of the list
L =[]
L.append(True)
print(L)
[True]
L
[True]
L.append(1.1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
L.append(1.1)
print(L)
[True, 1.1]
L.append(1024)
print(L)
[True, 1.1, 1024]
T = (-1,-2,-3)
L1 = [1.1,2.2,3.3]
L.append(T)
print(L)
[True, 1.1, 1024, (-1, -2, -3)]
L.append(L1)
print(L)
[True, 1.1, 1024, (-1, -2, -3), [1.1, 2.2, 3.3]]
len(L)
5
L[0]
True
L[1]
1.1
L[2]
1024
L[3]
(-1, -2, -3)
L[4]
[1.1, 2.2, 3.3]
L[5]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    L[5]
IndexError: list index out of range
#extend() function accepts only container objects and it adds al eleemnts in a container
#object as a separate element in the list
L = [10,20,30]
T = (10,20,30,40,50)
len(L)
3
L.append(T)
print(L)
[10, 20, 30, (10, 20, 30, 40, 50)]
len(L)
4
L.extend(T)
print(L)
[10, 20, 30, (10, 20, 30, 40, 50), 10, 20, 30, 40, 50]
len(L)
9
T1 = ((1.1,2.2,3.3),(4.4,5.5,6.6),(7.7,8.8,9.9))
L
[10, 20, 30, (10, 20, 30, 40, 50), 10, 20, 30, 40, 50]
L.append(T1)
print(L)
[10, 20, 30, (10, 20, 30, 40, 50), 10, 20, 30, 40, 50, ((1.1, 2.2, 3.3), (4.4, 5.5, 6.6), (7.7, 8.8, 9.9))]
len(L)
10
L.extend(T1)
print(L)
[10, 20, 30, (10, 20, 30, 40, 50), 10, 20, 30, 40, 50, ((1.1, 2.2, 3.3), (4.4, 5.5, 6.6), (7.7, 8.8, 9.9)), (1.1, 2.2, 3.3), (4.4, 5.5, 6.6), (7.7, 8.8, 9.9)]
len(L)
13
L.extend(10)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    L.extend(10)
TypeError: 'int' object is not iterable
