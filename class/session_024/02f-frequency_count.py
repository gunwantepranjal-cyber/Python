'''
@author : Pranjal Gunwante
@date   : 29 May 2026
@goal   : To solve frequency count problem printing all unique elements in list along with their frequency count
'''
#Given list : few integers occur more than once
L = [10,20,30,10,40,50,20,30,10,10,10,40,60,110,200]
#out while loop scans through the entire list in an index-wise fashion

#i is outer loop variable
i = 0
while i < len(L):
    #Part 1 : L[i] is the current element.Find out whether or not it was encountered before
    #the current index
    #Take j as inner loop variable and flag to indicate status
    current_data = L[i]
    found_flag = False
    #J should loop from 0 to i - 1
    j = 0
    while j < i:
        if current_data == L[j]:
            found_flag = True
            break
        j = j + 1

    #Part 2 : At this point found_flag will tell me whether or not current element was encountered
    #before the current index
    #If it was not encountered then the current element has occured for the first time
    #therefore , count its frequency, How ? loop from i to len(L) - 1 , compare and if equal increment the frequency_count
    if found_flag == True:
        i = i + 1
        continue
    frequency_count = 0
    j = i
    while j < len(L):
        if L[j] == current_data:
            frequency_count = frequency_count + 1
        j = j + 1
    print(f'Unique element:{current_data},frequency count:{frequency_count}',)
    i = i + 1