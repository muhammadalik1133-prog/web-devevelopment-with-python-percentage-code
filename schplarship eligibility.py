# Student E ligibility sysytem!
marks=int(input("Enter your total  marks out of 100:"))
att=int(input("Ente your attendence in %:"))
quiz=int(input("Enter quiz marks out of 10:"))
assignment=int(input("Enter assignment marks out of 10:"))
mid=int(input("Enter mid marks out of 30:"))
final=int(input("Enter final marks 50:"))

if (marks>=80 and marks<100) and (att>=85 and att<=100) and (quiz>=7  and quiz<=10) and (assignment>=7 and assignment<=10) and (mid>=25 and mid<=30) and (final>=45 and final<=50):
    print("Excellent performance- Eligible for 100% scolarship")

elif (marks>=70 and marks<80) and (att>=80 and att<=85) and (quiz>=6 and quiz<=7) and (assignment>=6 and assignment<=7) and (mid>=20 and mid<=25) and (final>=40 and final<=45):
    print("Best performance- Eligible for 90% scolarship")

elif (marks>=60 and marks<70) and (att>=70 and att<=80) and (quiz>=5 and quiz<=6) and (assignment>=5 and assignment<=6) and (mid>=18 and mid<=20) and (final>=35 and final<=40):
    print("Very good performance- Eligible for 80% scolarship")

elif marks>=50 and att<70:
    print("Average - Not eigible for scolarship and in warnings of SOA")
else:
    print("Not allowed to sit in Exams!")
    