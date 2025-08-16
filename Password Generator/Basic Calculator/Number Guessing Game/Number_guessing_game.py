import random
print("Hello user! Welcome to the number guessing game :)")
play = input("Do you want to play?(yes/no)").lower()
if play != "yes":
    print("Thanks for playing!")
    exit()
print("Let's start the game!")
while True:
    secret_number = random.randint(1,50)
    print("I have selected a number between 1 and 50.")
    while True:
        guess = int(input("What is your guess?"))
        if guess < secret_number:
            print("Your guess is lower")
        elif guess > secret_number:
            print("Your guess is higher")
        else:
            print("Hooray! You Guessed it!")
            break
    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break    

