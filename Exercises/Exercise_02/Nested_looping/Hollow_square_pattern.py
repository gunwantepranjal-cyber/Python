'''
    @data : 28 May 2026
    @Author : Pranjal Gunwante
    @Goal : Hollow Square pattern
'''
n = int(input("Enter number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or j == 1 or i == n or j == n :
            print("*",end="\t")
        else:
            print(" ",end ="\t")
        
    print()
