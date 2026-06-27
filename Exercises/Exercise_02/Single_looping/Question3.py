#Multiplication table of 7
print("Multiplication table using  for range loop :")
num = 7
for i in range(1,11):
    res = num * i
    print(num ,"*" , i ,"=",res)
print()

print("Multiplication table using  while loop :")
i = 0
while i <= 10:
    result = num * i
    i = i + 1
    print(num," * ",i," = ",result)
print()
print("Multiplication table using  for in loop:")
l = [ 1,2,3,4,5,6,7,8,9,10]
for i in l:
    result = num * i
    print(num , "*",i,"=",result)
    
