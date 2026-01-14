#Nested decisions in python
#for multi decisions
print("welcome to netflix")
name=input("Enter your name:")
email=input("Enter your email:")
password=input("Enter your password:")
age=int(input("Enter your age:"))
if age>=18:
     print(f"Dear {name}, welcome to netflix")
     if email=="muhammadalik1133@gmail.com" and password=="1234":
        print(f"Dear {name},Please select Category")
     
     elif email=="Azharelahi276@gmail.com" and password=="12345":
        print(f"Dear {name},Please select Category")
     
     elif email=="muhammadalik117@gmail.com" and password=="123456":
        print(f"Dear {name},Please select Category")
     
     elif email=="muhammadfaisalelahi556@gmail.com" and password=="1234567":
        print(f"Dear {name},Please select Category")
             
     else:
        print(f"Dear {name}, Your login credentials are invalid!")
     
     
else:
    print(f"Dear {name}, Please watch pogo")
  
