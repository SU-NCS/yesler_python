import Episode
import Creature
import Utils as ut 
import Player 
import Game 
import random

def challenge_1(num):
        guess = None
        guess = input("Give me a number between 1 and 10")
        try:
            guess = int(guess)
            if guess == num:
                return True
            elif guess < num:
                print("Try higher")
            elif guess > num:
                print("Try lower")
        except:
            print("That was not a number. Try again")
        return False

c = Creature.Creature("Billy", "Hi there", "No greeting", "no story")
n = random.randint(1,10)
success = False
while not c.is_hostile and not success:
    success = c.offer_challenge(challenge_1(n))


