import random

def main():
    print("=== Guessing Game ===")
    number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10 :"))

    if guess == number:
        print("You guessed right !")
    else:
        print(f"Wrong ! The number was {number}.")
main()