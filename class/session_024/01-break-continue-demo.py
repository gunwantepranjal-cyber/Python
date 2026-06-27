'''
@author : Pranjal Gunwante
@date   : 29 May 2026
@goal   : To Demonstrate break and continue 

'''
print("Start - Break Demo - with while loop")
L = [10,20,30,40,56,60,70,80]
#Travel the list using while loop and if the number in the list is divisible by 7 
#then abandon the loop(stop the current repeatation and cancel all sub-sequent repeatitions)

i = 0
while i < len(L):
    if L[i] % 7 == 0:
        break
    print(f'L[{i}]:L[{i}]')
    i = i + 1
print("End - break demo - with while loop")

print("start - break demo - with for loop")
for x in L:
    if x % 7 == 0:
        break
    print(f'x:{x}')
print("End - break demo with for loop")

print("Start - continue demo with for loop")
for x in L:
    if x % 7 == 0:
        continue
    print(f'x:{x}')
print("End - continue demo - with for loop")

print("start continue demo with while loop")

i = 0
while i < len(L):
    if L[i] % 7 == 0:
        i = i + 1
        continue
    print(f'L[{i}]:L[{i}]')
    i = i + 1
print("End coninue demo - with while loop")