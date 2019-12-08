# Practice FIle-Python Activity Code
Subject=(input("Enter the subject name:"))
Exam=float(input("Enter the marks obtained in Exam "+Subject))
CW=float(input("Enter the marks obtained in course work:"))
Percentage= (Exam+CW)/2
print("The Average Percentage of",Subject,":", Percentage)
if Percentage<60:
    print("Fails")
elif Percentage >= 60:
    print("Congratulation you have passed the exam")
