a = 7
b = 3
c = 5
result = a > b and b < c or not(a == c) and(a + b) % c == 0
print("result:",result)
if result:
    final_value = a * b +c
else:
    final_value = a + b - c
print("final value:",final_value)
print("Type check:",type(final_value).__name__)
