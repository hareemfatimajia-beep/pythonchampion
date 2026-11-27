import random
playiny = True
number = str(random.randint(0,19))

print("I will generate a number from 0 to 19, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playiny:
    guess = (input("Give your best guess"))
    if number == guess:
        print("You win the game")
        print("The number was",number)

    if number < guess:
        print("Too low")
    if number > guess:
        print("Too high")
        
    else:
        print("Your guess isn't quite right, try again.")



