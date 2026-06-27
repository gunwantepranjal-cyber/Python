#Max element in list
L = [10,20,30,40,80,40,67,110,51]
max_val = L[0]
print("Max element using for range loop:")
for i in range(0,len(L)): 
    if L[i] > max_val:
        max_val = L[i]
print("maximum element is:",max_val)
print()

print("Max elemnt using for in loop:")
max_val1 = L[0]
for i in L:
    if i > max_val1:
        max_val1 = i
print("maximum element is:",max_val1)
print()

print("Max element using while loop:")
max_val2 = L[0]
i = 0
while i < len(L):
    if L[i] > max_val2:
        max_val2 = L[i]
    i = i + 1

print("maximum element is:",max_val2)
print()

