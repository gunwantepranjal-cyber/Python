def my_sqrt(n):
    if type(n) != int and type(n) != float:
        raise TypeError(f'input must be int or float but received {type(n).__name__}')
    
    if n < 0:
        raise ValueError(f'Expected non negative integer or float')
    return n ** 0.5

r = my_sqrt(100)
print(r)
my_sqrt(-4) #ValueError
my_sqrt(5.4)
my_sqrt(-4.5)
my_sqrt(False)
my_sqrt("Hello")