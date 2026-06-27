N = int(input("Enter positive integer:"))
print("Start loop")
i = 0
while i < N:
    j = i
    print(f'Outer loop value:i:{i}')
    while j <= N:
        print(f'\t Inner loop variable j:{j}')
        j = j + 1
    i = i + 1
print('End loop')
