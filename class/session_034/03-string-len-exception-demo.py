def myFunc(s):
    if type(s) != str:
        raise TypeError(f'Expected string but received{type(s).__name__}')
    if len(s) != 10:
        raise ValueError(f'Length of input string must 10 but received String of len {len(s)}')
    print("Logic on string of length 10")

myFunc("hellohello")

def myFunc(s:str)->int:
    print(s)

myFunc(100)
myFunc([10,20,30])
myFunc(True)
myFunc(10,10)
