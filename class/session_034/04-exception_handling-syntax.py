def my_sqrt(n):
    if type(n) != int and type(n)!=float:
        raise TypeError(f'input must be int or float but recieed {type(n).__name__}')
    if n < 0:
        raise ValueError(f'Expected non negative integer or float')
    return n ** 0.5

try:
    print("strar of try block")
    my_sqrt("Hello")
    print("End of try block")
except TypeError:
    print("Start of except block")
    print("Sorry shaktiman sent argument of wrong type")
    print("End of except block")

print("Maze pudhil aayushya")