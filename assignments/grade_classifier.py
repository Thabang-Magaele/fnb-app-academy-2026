#Collect learner name and marks for three subjects (as floats) using input()
#Calculate the average mark across the three subjects
#Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
#Assign Pass status if the average is 50 or above, Fail otherwise
#Flag any individual subject mark below 40 as ‘needs intervention’
#Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags

full_name = input("Enter your name and surname: ").strip()
subject1 = float(input("Enter your mark for Subject 1: "))
subject2 = float(input("Enter your mark for Subject 2: "))
subject3 = float(input("Enter your mark for Subject 3: "))

#Claculate average mark
average_mark = (subject1 + subject2 + subject3) / 3

#Assigning a letter grade
if average_mark >= 80:
    letter_grade = "A"
    status = "Pass"

elif average_mark >=70 and average_mark <=79:
    letter_grade = "B"
    status = "Pass"

elif average_mark >=60 and average_mark <=69:
    letter_grade = "C"
    status = "Pass"

elif average_mark >=50 and average_mark <=59:
    letter_grade = "D"
    status = "Pass"

else:
    letter_grade = "F"
    status = "Fail"

if subject1 <40:
    attention = "subject 1 NEEDS ATTENTION"
elif subject2 <40:
    attention = "subject 2 NEEDS ATTENTION"
elif subject3 <40:
    attention = "subject 3 NEEDS ATTENTION"
else:
    attention = "No attention needed"

print ("\nReport Card")
print ("======================================")
print (f"Full Name: {full_name}")
print (f"Subject 1 mark: {round(subject1, 2)}")
print (f"Subject 2 mark: {round(subject2, 2)}")
print (f"Subject 3 mark: {round(subject3, 2)}")
print ("======================================")
print (f"Average Mark: {round(average_mark, 2)}")
print (f"Grade Symbol: {letter_grade}\nStatus: {status}\nIntervention Flags: {attention}")