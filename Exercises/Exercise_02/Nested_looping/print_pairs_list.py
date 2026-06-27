'''
    @data : 28 May 2026
    @Author : Pranjal Gunwante
    @Goal : print all pairs from list
'''
list1 = [1,2,3]
list2 = ['a','b','c']
for i in range(0, len(list1)):
    for j in range(0,len(list2)):
        print(f'({list1[i]},{list2[j]})')
