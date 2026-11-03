print("Chose your vacation")
print("Option 1 . water park")
print("Option 2 . zoo")

choice =int(input(" Enter 1 or 2"))

if choice == 1:
    print("Chose your water park")
    print("Option 1 . indoor")
    print("Option 2 . outdoor")

    water_choice = int(input("Enter 1 or 2"))

    if water_choice == 1:
        print("You picked : indoor")
        print("You can stay for : 2 hours")

    else:
        print("You picked : outdoor")
        print("You can stay for : 2 hours")

elif choice == 2: 
    print("You chose zoo")
    print("Option 1 . indoor")
    print("Option 2 . outdoor")

    zoo_choice = int(input("Enter 1 or 2"))

    if zoo_choice == 1:
        print("You picked : indoor")
        print("You can stay for : 2 hours")

    else:
        print("You picked : outdoor ")
        print("You can stay for : 2 hours")
