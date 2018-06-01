import Creature, Episode, Player
import Utils as ut 
import json 
import os 
import random # for episode 1.

def main(story):
   # Load game data
   try:
      with open(story) as f:
         game_data = json.load(f)
         print("Story Loaded...ready to begin.")
   except Exception as e:
      print("File problem: {}".format(e))
      print("Exiting.")

   
   # Import our challenges
   try:
      import challenges 
   except ImportError as e:
      print("Error loading challenges.")
      print("Exiting.")
   
   
   # Begin the Game
   ut.slow_print("Welcome to the Adventure Game in Text")
   print("The Rules are Simple: Get through the rooms and stay alive.")
   print("To get started, let's hear a little about you: ")
   
   # Initialize Player
   player = Player.Player()

   print("You start off with an empty knapsack:")
   for i in player.knapsack:
      print(i)
   print("You have {} hitpoints".format(player.hitpoints))
   
   ut.slow_print(game_data['introduction'])
   # While loop for multiple episodes.
   # Initialize Episode
   episode_data = game_data["episodes"][0]
   episode = Episode.Episode(episode_data)
   episode.print_narrative()
   ut.slow_print("You enter the room.")
   episode.describe_room()
   reply = input("Do you want to look for treasure? (Y/n) ")
   if reply.lower() != "n":
      result = episode.get_treasure()
   player.hitpoints += result[0]
   player.add_item(result[1])

   # Initialize Creature
   creature_data = game_data["creatures"][0]
   creature = Creature.Creature(creature_data)

   print("There's a creature in the room.")
   creature.describe()
   reply = input("Do you want to greet {}? (Y/n)".format(creature.name))
   if reply.lower() != "n":
      creature.greet()
      creature.tell_story()
   
   print("{} wants to offer you a challenge to get out of the room.".format(creature.name))
   reply = input("Do you accept? (Y/n)")
   if reply.lower() != "n":
      success = False
      chal = challenges.Episode1()
      while not creature.is_hostile and not success:
         success = creature.offer_challenge(chal)
   
   if success:
      print("YOU WIN!")
   else:
      print("YOU NEED TO TRY THIS ROOM AGAIN. THE MONSTER'S PISSED.")
   

main('test_game.json')