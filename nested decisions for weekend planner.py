#weekend planner
print("Welcome to weekend planner:")
name=input("Enter your name:")
mood=input("Enter your mood(happy/sad/tired):").lower()
budget=int(input("Enter your budget ($):"))
weather=input("Weather today? (sunny/rainy/cold):").lower()
company=input("Who are you with? (alone/friends/family):").lower()
print("planning weekend")
if mood=="happy":
    if budget>1000:
        if weather=="sunny":
            if company=="friends":
                print(f"Dear {name}, go For an outdoor movie+ street food party!")
            else:
             print("watch blockbuster movie!")
        else:
            print("order pizza + netfilx at home!")
        
    else:
        print("watch coomedy movie on mobile with snacks!!")

elif mood=="sad":
    if company=="alone":
        print("watch motivational movie and order comfort food!")
    else:
        if budget>500:
            print("Ice cream + feel good movie with loved ones!")
        else:
            print("tea + old classic movie!")

elif mood=="tired":
    if weather=="cold":
        print("sleep early + light music!")
    else:
        if budget>300:
            print("Fast food + and watch comedy show!")
        else:
            print("Relax with music or book!")
else:
    print("Mood not recognized")

        
    
