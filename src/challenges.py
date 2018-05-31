def episode1(num):
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