import random
chances = 0 
number = random.randint(1,9)

while chances<5:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("Congratulations! You won!")
        break
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    chances+=1

if not chances < 5:
    print("You lose! The number is", number)
