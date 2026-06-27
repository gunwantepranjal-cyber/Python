score1 = 85
score2 = 92
score3 = 78
average = (score1 + score2 + score3)/3
print("Average",average)
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else :
    grade = 'F'
print("Grade:",grade)
print("Pass" if grade != "F" else "fail")

    
