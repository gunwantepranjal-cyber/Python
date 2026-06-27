#Reverse list
L1 = [10,20,30,40,50]
L2 = [0] * len(L1)
k = 0
length = len(L1)
print("Original list is :",L1)
print("reverse list using for range loop:")
for i in range(0,length):
    L2[k] = L1[length - k - 1]
    k = k+1
    
for x in L2:
    print(x)
print()

print("reverse list using for in loop:")
L3 =[0] * len(L1)
k = 0
for i in L1:
    L3[k] = L1[length - k -1]
    k = k+1
    
for x in L3:
    print(x)
print()

print("reverse list using while loop:")
L4 =[0] *len(L1)
k = 0
i = 0
while i < length:
    L4[i] = L1[length - i - 1]
    i = i + 1
for i in L4:
    print(i)



    
