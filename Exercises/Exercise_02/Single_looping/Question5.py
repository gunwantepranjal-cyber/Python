#Factoraial
num = int(input("Enter number:"))
print("Factorial using for range loop")
fact = 1
for i in range(1 , num+1):
    fact = fact * i
print("Factorial of ",num,"is",fact)
print()

print("Factorial using while loop:")
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of ",num,"is",fact)
print()

print("Factorial using for in loop:")
fact = 1
L4 = [0] * num
k = 0
for i in range(1,num+1):
    L4[k] = i
    k = k + 1
    
for i in L4:
    fact = fact * i
print("Factorial of ",num,"is",fact)
print()
    
