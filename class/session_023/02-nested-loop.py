M = int(input("Enter positive integer:"))
N = int(input("Enter positive integer:"))
print("Start of loop")
i = 0
while i < M:
    print(f'OUter loop variable:i:{i}')
    j = 0
    while j < N:
         print(f'OUter loop variable:i:{i}')
         print(f'Inner loop variable:i:{j}')
         j = j + 1
    i = i + 1
print("End of loop")
