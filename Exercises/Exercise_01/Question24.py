p = True
q = False
r = True
result1 = p and q or r
result2 = p and (q or r)
print(result1)
print(result2)
print(result1 == result2)
