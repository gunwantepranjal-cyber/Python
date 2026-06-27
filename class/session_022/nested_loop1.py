total_bunny_rounds = 0
tortoise_rounds = 0
while tortoise_rounds < 8:
    print(f'Tortois rounds : {tortoise_rounds}')
    bunny_rounds = 0
    while bunny_rounds < 5:
        print(f'Bunny rounds : {bunny_rounds}')
        total_bunny_rounds = total_bunny_rounds + 1
        bunny_rounds = bunny_rounds + 1
    print(f'Total bunny rounds : {total_bunny_rounds}')
    tortoise_rounds = tortoise_rounds + 1