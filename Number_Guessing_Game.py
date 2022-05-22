import random
lower = int(input("Lower Bound: "))
upper = int(input("Upper Bound: "))

number = random.randint(lower,upper)
tries = 1
guess = int(input("Guess A Number: "))

while guess != number:
    
    if guess < number:
        print("Underestimated.")
    elif guess > number:
        print("Overestimated.")
    guess = int(input("Guess A Number: "))
    tries += 1
    
print("Congrats! You did it in ",tries," try.")

