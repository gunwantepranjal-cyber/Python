#sum of all natural numbers
sum = 0
print("sum of nubers using for range loop :")
num = int(input("Enter the number:"))
for i in range(1,num+1):
    sum = sum + i
print("sum is:",sum)
print()

print("sum of numbers using while loop:")
sum2 = 0;
i = 1;
while i <= num:
    sum2 = sum2 + i
    i = i + 1
print("sum is:",sum2)
print()


