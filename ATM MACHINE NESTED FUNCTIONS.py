#ATM Transaction System

print("******--------ATM Machine----------*******")

balance=5000
users=1
pin=1234
while users<=2:
    print(f"User No# {users}")
    
    user_pin=int(input("Enter your PIN:"))
    
    if user_pin==pin:
        attempts=0
        while attempts<3:
            print(f"\n------ Main Menu (attempts {attempts +1})----")
            print("\n1. Check Balance \n2. Withdraw Money \n3. Deposite Money \n4. Mini Statment \n5. Exit")
            choice=int(input("Choose Option:"))
            
            #nested-if-else
            if choice==1:
                print(f"Your Current Balane {balance}")
                
            elif choice == 2:
                amount = int(input("Amount to Withdraw:"))
                
                #nested if in withdraw
                
                if amount <= balance:
                    balance -= amount
                    print(f"Withdraw Amount {amount}")
                    print(f"Remaining Balance is {balance}")  
#                     if amount <=5000:
#                         balance = balance -1
#                         print(f"Withdraw Amount {amount}")
#                         print(f"Remaining Balance is {balance}")
                else:
                    print("MAximum Withdrawl Limit is 5000!")
            else:
                print("Insufficient balance!")
    elif choice==3:
        amount=int(input("Enter your amount to deposit:"))
                
        if amount>0:
            if amount<=balance:
                 balance += amount
                 print(f"Deposited amount {amount}")
                 print(f"New Balance is {balance}")
            else:
                print("Maximum Deposit Limit i.e Rs. {balance} is is Reached!")
        else:
            print("Invalid Amount!")
                    
    elif choice==4:
                #Nested for loop -Mini Statment
                print("Mini Statment")
                transaction=["Salary", "Groceries", "Bills", "Savings"]
                amounts=[5000, -500, -1000, 2000]
                
                for i in range(len(transaction)):
                    print(f"{transaction [i]}: Rs. {amount[i]}")
                    
    elif choice==5:
                print(f"Thank you for Banking us!")
                break
    else:
        print("Invalid Option!")
                
    attempts +=1
            
    if attempts >=3:
        print("Maximum Attempt Reached!")
    else:
        print("Sysyem Error!")
else:
    print("Wrong Pin!")
        
    users +=1    
                    
print("*********ATM is Stutting Down*********")