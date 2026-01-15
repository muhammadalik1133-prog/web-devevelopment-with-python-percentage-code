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
    
        
    
    
elif select==3:
    print("Welcome to car recommendation system")
    name=input("Please enter your name:")
    
else:
    print("Invalid input!") 