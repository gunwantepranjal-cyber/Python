#count digits in a number
num = 12345
count1 = 0
print("Count digits using while loop :")
while num > 0:
    num = num // 10
    count1 = count1 + 1
print("count of digits are :",count1)
print()

print("Count digits using for range loop:")
num2 = 1432765
count2 = 0
for i in range(num2):
    if num2 == 0:
        break
    num2= num2 // 10
    count2 = count2 + 1
print("count of digits are :",count2)
print()

print("Count digits using for in loop :")
num3 = '5432090'
count3 = 0
value_list = list(num3)
for i in value_list:
    count3 = count3 + 1
print("count of digits are:",count3)
