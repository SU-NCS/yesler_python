import random

def challenge_1():
        guess = None
        num = random.randint(1,10)
        for i in range(10):
            guess = input("Give me a number between 1 and 10")
            guess = int(guess)
            if guess == num:
                return True
            elif guess < num:
                print("Try higher")
            elif guess > num:
                print("Try lower")
            
        print("That was not a number. Game over")
        return False