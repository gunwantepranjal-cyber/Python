'''
    @data : 28 May 2026
    @Author : Pranjal Gunwante
    @Goal : Matrix row sum
'''
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(list1)):
    sum = 0
    for j in range(0,len(list1[i])):
        sum = sum + list1[i][j]
    print("sum :",sum)