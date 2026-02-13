print("multiple app player")
select=int(input("Select an app you want to work: \n1.Calculator \n2. Student marksheet \n3.clothing store \n4.car recommenation system:"))
if select==1:
    method=input("what you want to do?: \n1.Addition \n2.Substraction \n3.division \n4.multiplication:")
    num1=eval(input("Enter number 1 to proceed:"))
    num2=eval(input("Enter number 2 to proceed:"))
    if method=="1":
        print(f"This is your addition: {num1+num2}")
    elif method=="2":
        print(f"This is your substraction: {num1-num2}")
    elif method=="3":
        print(f"This is your division: {num1/num2}")
    elif method=="4":
        print(f"This is your multiplication: {num1*num2}")
    else:
        print("Enter a valid input!")

elif select==2:
    print("Welcome to marks sheet")
    name=input("please enter your name:")
    rollno=int(input("Enter your roll number:"))
    maths=int(input("Enter your maths number out  of 100:"))
    bio=int(input("Enter your biology marks out of 100:"))
    physics=int(input("Enter your physics number out of 100:"))
    chem=int(input("Enter your chemistry marks out of 100:"))
    urdu=int(input("Enter your urdu marks out pf 100:"))
    eng=int(input("Enter your english marks ouut of 100:"))
    islam=int(input("Enter your islamiyat marks out of 100:"))
    pak=int(input("enter your pak studies marks out of 100:"))
    obtain=maths+bio+physics+chem+urdu+eng+islam+pak
    total=800
    percentage=(obtain/total*100)
    if (percentage>=85 and percentage<100):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain A+ grade")
    
    elif (percentage>=80 and percentage<85):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain A+ grade")
    
    elif (percentage>=75 and percentage<80):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain B+ grade")
    
    elif (percentage>=70 and percentage<75):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain B grade")
    
    elif (percentage>=65 and percentage<70):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain B- grade")
    
    elif (percentage>=60 and percentage<65):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain C+ grade")
    
    elif (percentage>=55 and percentage<60):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain C grade")

    elif (percentage>=50 and percentage<55):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain C- grade")
    
    elif (percentage>=45 and percentage<50):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain D+ grade")
    
    elif (percentage>=40 and percentage<45):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain D grade")
    
    elif (percentage>=35 and percentage<40):
     print(f"Dear {name},Your total marks are {total}, \n.you obtained {obtain} marks, \n.your percentage is {percentage}, \n.you obtain D- grade")
    else:
       print(f"Dear {name}, You are fail.")
    
    
elif select==3:
    print("Welcome to online clothing store")
    name=input("Please enter your name:")
    email=input("enter your email:")
    budget=int(input("enter your budget minimum limit is 5000PKR:"))
    print("Recommended wears according to your budget")
    if (budget>=5000 and budget<=10000):
     print(f"Dear {name}, according to your budget whis is {budget},we recommend semi casual wear:")
    
    elif (budget>10000 and budget<=20000):
     print(f"Dear {name}, according to your budget whis is {budget},we recommend casual wear:")
    
    elif (buget>20000 and budget<=35000):
     print(f"Dear {name}, according to your budget whis is {budget},we recommend formal wear:")
    elif (budget>35000):
     print(f"Dear {name}, we recommend you all kinds of wear:")

    else:
        print("Sorry! you have insufficient balance")

elif select==4:
    print("welcome to car recommendation system")
    name=input("Enter your name:")
    email=input("Enter your email:")
    budget=int(input("Enter your budget,minimum limit is 500000:"))
    cartype=input("which car type you want, press accordingly,\n1.for sedan: \n2:for SUV:")
    sitting=int(input("please enter the sitting capacity from 1-8:"))
    gear=input("enter the car type you want ,(auto/manual):").lower()
    sunrooof=input("You want sunroof or not , for sedan press no , for SUV press no or yes:").lower()
    cc=int(input("please enter the engine cc you want , for sedan choose from(800-1200) for suv choose from (1200-2000):"))
    if (budget>=500000 and budget<1500000) and cartype==1 and sitting>1 and sitting<8 and gear=="manual" and sunroof=="no" and cc>=800 and cc<1200:
     print(f"Dear customer,according to your budget which is {budget},we have three cars available for you \n1.Suzuki mehran \n2. coure \n3.Suzuki Alto:")
    
    elif (budget>=1500000 and budget<25000000) and cartype==1 and sitting>1 and sitting<8 and gear=="auto" and sunroof=="no" and cc>=800 and cc<1200:
     print(f"Dear customer,according to your budget which is {budget},we have three cars available for you \n1.Suzuki Alto \n2.Toyota AQUA \n3.Suzuki Wagoner:")
    
    elif (budget>=2500000 and budget<35000000) and cartype==2 and sitting>1 and sitting<8 and gear=="auto" and sunroof=="no" and cc>=1200 and cc<2000:
     print(f"Dear customer,according to your budget which is {budget},we have three cars available for you \n1.Toyota corrolla \n2.Honda Civic \n3.Honda city:")
    else:
        print("Please enter correct information")
else:
    print("Invalid input!") 