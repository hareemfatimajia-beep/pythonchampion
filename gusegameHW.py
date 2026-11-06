import random

secret_number = random.randint(1, 50)
lives = 5

print("🎮 Number Guessing Game")
print("Guess the secret number between 1 and 50.")
print("You have 5 attempts.\n")

while lives > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        break

    lives -= 1

    if lives > 0:
        if guess < secret_number:
            print("📈 Too low!")
        else:
            print("📉 Too high!")

        print("Lives left:", lives)
    else:
        print("\n❌ Game Over!")
        print("The secret number was:", secret_number)
