print("Start demo - 1")
i = 0
while i < 3:
    print(f'Outer loop:i:{i}')
    j = 0
    while j < 4:
        print(f'Outer loop:i:{i},Inner loop: j:{j}')
        j = j + 1
    i = i +  1
print("End demo - 1")
