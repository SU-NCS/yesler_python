# def episode1(num):
#    guess = None
#    guess = input("Give me a number between 1 and 10")
#    try:
#       guess = int(guess)
#       if guess == num:
#          return True
#       elif guess < num:
#          print("Try higher")
#       elif guess > num:
#          print("Try lower")
#    except:
#       print("That was not a number. Try again")
#    return False


# def episode2():
#       pass

import random

class Episode1(object):
      num = 0
      
      def __init__(self):
            self.num = random.randint(1,10)
      
      def guess(self):
            in_guess = input("Give me a number between 1 and 10")
            try:
                  in_guess = int(in_guess)
                  if in_guess == self.num:
                     return True
                  elif in_guess < self.num:
                     print("Try higher")
                  elif in_guess > self.num:
                     print("Try lower")
            except:
               print("That was not a number. Try again")
            return False