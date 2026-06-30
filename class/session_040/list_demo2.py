Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import sys
def main():
    line = "-" * 65
    #ways of creation
    #1
    print("Always of creation:")
    L = [True,10,3.14,(10,20,30)]
    print("L:",L)

    

print(L)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(L)
NameError: name 'L' is not defined
L = [True,10,3.14,(10,20,30)]
print("L:",L)
L: [True, 10, 3.14, (10, 20, 30)]
#2
T = (10,20,30)
s = "hey!"
S={10,20,30}
L1 = list(T)
L2 = list(s)
L2 = list(S)
print("L1:",L1)
L1: [10, 20, 30]
print("L2:",L2)
L2: [10, 20, 30]
print("L3:",L3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print("L3:",L3)
NameError: name 'L3' is not defined. Did you mean: 'L'?
L3 = list(s)
print(L3)
['h', 'e', 'y', '!']
print("(B):built-in functions")
(B):built-in functions
L = [10,20,30,40]
print("Print:L:",L)
Print:L: [10, 20, 30, 40]
print("type(L):",type(L))
type(L): <class 'list'>
print("id(L):",id(L))
id(L): 2209997142528
print("len(L)":len(L))
SyntaxError: invalid syntax
print("len(L):",len(L))
len(L): 4
s = '-' * 20
print(s)
--------------------
#Traversing through string
print("traverse:for loop 1")
traverse:for loop 1
L = [True,10,3.14,(100,200,300)]
for x in L:
    print(x,type(x))

    
True <class 'bool'>
10 <class 'int'>
3.14 <class 'float'>
(100, 200, 300) <class 'tuple'>
print(s)
--------------------
print("travers:for lop 2:index based")
travers:for lop 2:index based
for  i in range(len(L)):
    print("L[{}]:{},type(L[{}]:{}".format(i,L[i],i,type(L[i])))

    
L[0]:True,type(L[0]:<class 'bool'>
L[1]:10,type(L[1]:<class 'int'>
L[2]:3.14,type(L[2]:<class 'float'>
L[3]:(100, 200, 300),type(L[3]:<class 'tuple'>
#C Built in operators
                          
print("(C) Built in operators")
                          
(C) Built in operators
#Concatenation
                          
L1 =[10,20,30]
                          
L2 = [40,50,60]
                          
L3 = L1 + L2
                          
print("Concatination L3:",L3)
                          
Concatination L3: [10, 20, 30, 40, 50, 60]
#Multipication by scalar
                          
L = [10,20,30]
                          
L_3 = L * 3
                          
print("Multiplication by scalar:L_3",L,L_3)
                          
Multiplication by scalar:L_3 [10, 20, 30] [10, 20, 30, 10, 20, 30, 10, 20, 30]
#index , range slice(on RHS)
                          
L = [10,15,20,25,65,23,576,43,23,654,854,2476,754,643,22]
                          
print("index range and slice on RHS:")
                          
index range and slice on RHS:
print("len(L):",len(L))
                          
len(L): 15
print("index:L[3]",L[3])
                          
index:L[3] 25
print("index:L[3]",L[3])
                          
index:L[3] 25
print("index:L[3]:",L[3])
                          
index:L[3]: 25
print("index:L[-3]:",L[-3])
                          
index:L[-3]: 754
print("range:L[2:8]:",L[2:8])
                          
range:L[2:8]: [20, 25, 65, 23, 576, 43]
print("range:L[-12:-4]:",L[-12:-4])
                          
range:L[-12:-4]: [25, 65, 23, 576, 43, 23, 654, 854]
print("slice : L[2:14:3] : ",L[2:14:3])
                          
slice : L[2:14:3] :  [20, 23, 23, 2476]
print("slice : L[12:1:-2] : ",L[12:1:-2])
                          
slice : L[12:1:-2] :  [754, 854, 23, 576, 65, 20]
print("slice : L[::-1] : ",L[::-1])
                          
slice : L[::-1] :  [22, 643, 754, 2476, 854, 654, 23, 43, 576, 23, 65, 25, 20, 15, 10]
print(s)
                          
--------------------
#index,range , slice on LHS
                          
print("index,range,slice on LHS:")
                          
index,range,slice on LHS:
print("index:L[5]:",L[5])
                          
index:L[5]: 23
L[5] = 70000
                          
print(L[5])
                          
70000
print("range:L[7:11]:",L)
                          
range:L[7:11]: [10, 15, 20, 25, 65, 70000, 576, 43, 23, 654, 854, 2476, 754, 643, 22]
L[7:11] = (1000,2000,3000,4000)
                          
print(L[7:11])
                          
[1000, 2000, 3000, 4000]
print(L)
                          
[10, 15, 20, 25, 65, 70000, 576, 1000, 2000, 3000, 4000, 2476, 754, 643, 22]
print("slice:L[2:11:3]:",L)
                          
slice:L[2:11:3]: [10, 15, 20, 25, 65, 70000, 576, 1000, 2000, 3000, 4000, 2476, 754, 643, 22]
L[2:11:3] = "ABC"
                          
print("slice:L[2:11:3]:",L)
                          
slice:L[2:11:3]: [10, 15, 'A', 25, 65, 'B', 576, 1000, 'C', 3000, 4000, 2476, 754, 643, 22]
#in operator
                          
L = [100,200,300,400]
                          
b = (100 in L)
                          
print("100 in L:",b)
                          
100 in L: True
b (5000 in L)
                          
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    b (5000 in L)
TypeError: 'bool' object is not callable
b = (5000 in L)
                          
print(b)
                          
False
#(D) : css Methods
                          
#index method
                          
print(" ( D ) : class methods")
                          
 ( D ) : class methods
L = [10,20,30,40,50,60,10,70,80]
                          
n = L.index(10)
                          
print(n)
                          
0
m = L.index(10,n+1)
                          
print(m)
                          
6
k = L.index(10,m+1)
                          
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    k = L.index(10,m+1)
ValueError: list.index(x): x not in list
n = l.count(10)
                          
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    n = l.count(10)
NameError: name 'l' is not defined. Did you mean: 'L'?
n = L.count(10)
                          

print(n)
                          
2
#count method
                          
print("L.count(10):",L.count(10))
                          
L.count(10): 2
print(s)
                          
--------------------
print("append")
                          
append
L = []
                          
L.append(True)
                          
print(L)
                          
[True]
L.append(100)
                          
print(L)
                          
[True, 100]
T = (100,200,300)
                          
L.append(T)
                          
print(L)
                          
[True, 100, (100, 200, 300)]
len(L)
                          
3
print(s)
                          
--------------------
print("extend")
                          
extend
L.extend("T")
                          
print(L)
                          
[True, 100, (100, 200, 300), 'T']
s = "SEPARATE"
                          
L.extend(s)
                          
print(L)
                          
[True, 100, (100, 200, 300), 'T', 'S', 'E', 'P', 'A', 'R', 'A', 'T', 'E']
print("inser")
                          
inser
L = [100,200,300,400,500,600,700,800]
                          
pirnt("insert:L",L)
                          
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    pirnt("insert:L",L)
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print("insert:L",L)
                          
insert:L [100, 200, 300, 400, 500, 600, 700, 800]
L.insert(3,4000)
                          
print(L)
                          
[100, 200, 300, 4000, 400, 500, 600, 700, 800]
L.insert(0,-100)
                          
print(L)
                          
[-100, 100, 200, 300, 4000, 400, 500, 600, 700, 800]
L.insert(len(L),-200)
                          
print(L)
                          
[-100, 100, 200, 300, 4000, 400, 500, 600, 700, 800, -200]
L.insert(L.index(40000),-1)
                          
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    L.insert(L.index(40000),-1)
ValueError: list.index(x): x not in list
L.insert(L.index(4000),-1)
                          
print(L)
                          
[-100, 100, 200, 300, -1, 4000, 400, 500, 600, 700, 800, -200]
L.insert(L.index(4000)+1 ,-2)
                          
print(L)
                          
[-100, 100, 200, 300, -1, 4000, -2, 400, 500, 600, 700, 800, -200]
print("How to remove elements")
                          
How to remove elements
#index,range , slice deletion
                          
print("del index:L",L)
                          
del index:L [-100, 100, 200, 300, -1, 4000, -2, 400, 500, 600, 700, 800, -200]
del L[5]
                          
print(L)
                          
[-100, 100, 200, 300, -1, -2, 400, 500, 600, 700, 800, -200]
del L[2:7]
                          
print(L)
                          
[-100, 100, 500, 600, 700, 800, -200]
del L[1:6:2]
                          
print(L)
                          
[-100, 500, 700, -200]
#data basd removal
                          
L.remove(500)
                          
print(L)
                          
[-100, 700, -200]
L= [100,200,300,400,500]
                          
#pop = remove + return
                          
print("Pop : initial:L:",L)
                          
Pop : initial:L: [100, 200, 300, 400, 500]
n = L.pop()
                          
print(n)
                          
500
n = L.pop(2)
                          
print(n)
                          
300
#how to remove all elemnts from list?
                          
print("L:",L,"Id(L):",id(L))
                          
L: [100, 200, 400] Id(L): 2209996917056
L.clear()
                          
print(L)
                          
[]
print("L:",L,"Id(L):",id(L))
                          
L: [] Id(L): 2209996917056
#immutable reversal
                          
L = [100,200,300,400,500]
                          
LR = L[::-1]
...                           
>>> print(LR)
...                           
[500, 400, 300, 200, 100]
>>> print("reverse:L:",L)
...                           
reverse:L: [100, 200, 300, 400, 500]
>>> L.reverse()
...                           
>>> print(L)
...                           
[500, 400, 300, 200, 100]
>>> L = [100,4,322,55,66,32]
...                           
>>> LS = sorted(L)
...                           
>>> print(LS)
...                           
[4, 32, 55, 66, 100, 322]
>>> L.sort()
...                           
>>> print(L)
...                           
[4, 32, 55, 66, 100, 322]
>>> #copy method
...                           
>>> L[100,200,300,400,500]
...                           
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    L[100,200,300,400,500]
TypeError: list indices must be integers or slices, not tuple
>>> print(L)
...                           
[4, 32, 55, 66, 100, 322]
>>> print(id(L))
...                           
2209997383616
>>> LC = L.copy()
...                           
>>> print(LC)
...                           
[4, 32, 55, 66, 100, 322]
>>> print(id(LC))
...                           
2209997333248
