
# i = 0
# def tet_function():
#     i = i + 1

# tet_function()
#Warning principle : If you want to modify a global variable
#within a function then you must declare it to be global
#inside the function using 'global' statement provided by Python.

#Global Variable : Any variable that defined outside all functions
#and classes is a global variable in python.

i = 0
def test_function():
    global i
    i = i + 1
    print('i :',i)
test_function()


