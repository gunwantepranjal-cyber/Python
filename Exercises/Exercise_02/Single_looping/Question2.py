#count vowels in a string
str = "Hello World"
count = 0
print("Count vowel using for range  loop : ")
for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U':
        count = count+1
print("count of vowel is:",count)
print()

print("Count vowels using for in loop:")
count1 = 0
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
       count1 = count1 + 1
print("Count of vowels is : ",count1)
print()

print("Count of vowels using while loop:")
i = 0;
count3 = 0
l = len(str)
while i < l:
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U':
       count3 = count3 + 1
    i = i+1
print("Count of vowels is :",count3)
print()
    
