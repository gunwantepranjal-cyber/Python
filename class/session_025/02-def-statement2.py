'''
@author : Pranjal Gunwante
@date   : 2nd june 2026
@goal   : Def statement demo 2

'''
def is_even(n):
    b_flag = (n % 2== 0)
    return b_flag
b1 = is_even(10)
print(f'Return value of is_event(10):{b1}')
m = int(input("Enter an integer:"))
b2 = is_even(m)
print(f'Return value of is_event({m}):{b2}')
#-----------------------------------------------
def find_max(lst):
    max_number = lst[0]
    for i in range(1,len(lst)):
        if lst[i]> max_number:
            max_number = lst[i]
    return max_number
L1 = [10,20,30,40,50]
L2 = [1000,2000,3000,4,5]

n1 = find_max(L1)
n2 = find_max(L2)
print(f'Return value of find_max({L1}):{n1}')
print(f'Return value of find_max({L2}):{n2}')

def insertion_sort(lst):
    for j in range(1,len(lst)):
        key = lst[j]
        i = j - 1
        while i > -1 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key
def show_list(lst,msg):
    print(msg)
    for i in range(len(lst)):
        print(f'lst[{i}]:{lst[i]}')
L = [1000,20,3,200,400,500,23,41]
show_list(L,"Before Sort")
insertion_sort(L)
show_list(L,"After sort:")
                