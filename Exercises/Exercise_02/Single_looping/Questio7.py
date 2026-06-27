#sum of dictionary values
prices = {"apple":30,"orange":40,"banana":70,"strawberry":90}
print("sum using for in loop : ")
sum = 0;
for i in prices.values():
    sum = sum + i
print("sum of all fruits prices is :",sum)
print()

print("sum using for range loop:")
sum1 = 0
value_list = list(prices.values())
for i in range(0,len(prices)):
    sum1 = sum1 + value_list[i];
print("sum of all fruits prices is :",sum1)
print()

print("Sum using the while loop:")
sum2 = 0
i = 0
while i < len(prices):
    sum2 = sum2 + value_list[i]
    i = i+1
print("sum of all fruits prices is :",sum2)
