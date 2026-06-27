#triangle star pattern
print("Star pattern using for range loop:")
for i in range(1 , 5):
    for j in range(1,i+1):
        print("*",end =" ")
    print()

print("star pattern using while loop:")
i = 1
while i < 5:
    j = 1;
    while j <= i:
        print("*",end=" ")
        j = j + 1
   
    print()
    i = i + 1
    
   

