x = 3
y = 5
z = 2
max_val = x
if y > max_val:
    max_val = y
if z > max_val:
    max_val = z
print("Maximum value",max_val)
print("Is it greater than average",max_val > (x + y + z)/3)
