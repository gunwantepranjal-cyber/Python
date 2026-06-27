#Filter even numbers from list
L = [3,8,15,22,7,36,41,50,19,64]
L2 =[]
print("Original list:",L)
print("Filter even number using for range loop : ")
for i in range(0,len(L)):
    if L[i]% 2 == 0:
        L2.append(L[i])
print(L2)
print()
print("Filter even number using for in loop : ")
L3 = []
for i in L:
    if i %2 == 0:
        L3.append(i)
print(L3)
print()

print("Filter even number using while loop : ")
L4 = []
i = 0
while i < len(L):
   if L[i] % 2 == 0:
       L4.append(L[i])
   i = i + 1 
print(L4)

                

