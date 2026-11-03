print("Pick your vehichle")
print("Option 1 . bike")
print("Option 2 . car")

choice =int(input(" Enter 1 or 2"))

if choice == 1:
    print("Chose your bike type")
    print("Option 1 . electric scooter")
    print("Option 2 . bike mountain")

    bike_choice = int(input("Enter 1 or 2"))

    if bike_choice == 1:
        print("You picked indoor ")
        print("Top speed : 80 km")

    else:
        print("You picked : mountain bike")
        print("Top speed : 65 km")

elif choice == 2: 
    print("You chose car type")
    print("Option 1 . Sadan")
    print("Option 2 . SUV")

    car_choice = int(input("Enter 1 or 2"))

    if car_choice == 1:
        print("You picked : Sadan")
        print("Top speed : 85 km")

    else:
        print("You picked : SUV")
        print("Top speed : 95 km")
