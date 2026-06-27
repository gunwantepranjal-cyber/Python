N = int(input("Enter positive integer"))
print("start loop")
i = 0
while i < N:
    j = i + 1
    print(f'Outer loop value i :{i}')
    while j < N:
        print(f'Innter loop variable:j:{j}')
        j = j + 1
    i = i + 1
print('End loop')
