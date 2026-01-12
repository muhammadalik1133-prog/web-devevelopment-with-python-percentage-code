name=input("Enter your name:")
rollno=int(input("enter your roll number:"))
eng=int(input("enter your obtained english marks:"))
urdu=int(input("enter your obtained urdu marks:"))
isl=int(input("enter your obtained islamiyat marks:"))
phys=int(input("enter your physics marks:"))
chem=int(input("enter your chemistry marks:"))
bio=int(input("enter your biology marks:"))
obtain=eng+urdu+isl+phys+chem+bio
total=600
per=(obtain/total)*100
if per>=60 and per<=64:
    print(f"your total percentage is {per} and you obtainn obtain D- grade:")

elif per>=65 and per<=66:
    print(f"your total percentage is {per} and you obtainn obtain D grade:")

elif per>=67 and per<=69:
    print(f"your total percentage is {per} and you obtainn obtain D+ grade:")

elif per>=70 and per<=74:
    print(f"your total percentage is {per} and you obtainn obtain C- grade:")

elif per>=75 and per<=76:
    print(f"your total percentage is {per} and you obtainn obtain C grade:")

elif per>=77 and per<=79:
    print(f"your total percentage is {per} and you obtainn obtain C+ grade:")

elif per>=80 and per<=84:
    print(f"your total percentage is {per} and you obtainn obtain B- grade:")

elif per>=85 and per<=86:
    print(f"your total percentage is {per} and you obtainn obtain B grade:")

elif per>=87 and per<=89:
    print(f"your total percentage is {per} and you obtainn obtain B+ grade:")

elif per>=90 and per<=94:
    print(f"your total percentage is {per} and you obtainn obtain A- grade:")

elif per>=95 and per<=100:
    print(f"your total percentage is {per} and you obtainn obtain A+ grade:")
else:
    print(f"your total percentage is {per} and you are fail:")
    
   
    







