L = [10,20,30,40]
print("Using for loop")
for x in L:
    print(x)
print("Using while loop")
i = 0
while i < len(L):
    print(i,L[i])
    i = i+1
print("using for loop method 2")
for i in range(len(L)):
    print(i,L[i])
print("___done using three method____")
