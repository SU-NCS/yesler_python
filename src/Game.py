import json
import time
import os
import Player
import Episode
import Utils as ut

class Game:

    def __init__(self, story, challenge_path):
        self.player = Player.Player()
        try:
            with open(story) as f:
                self.game_data = json.load(f)
                print("Success. Story loaded.")
        except Exception as e:
            print("Something went wrong with your file. I need a story: {}".format(e))
        # Import our challenges
        try:
            for root, dirs, files in os.walk(challenge_path):
                __all__ = [name.split(".")[0] for name in files if "challenge" in name]
                
        except Exception as e2:
            print("There's something wrong with your challenge path: {}".format(e))

    def start_game(self):
        counter = len(self.game_data) #number of episodes
        #print ("counter",counter)
        while self.player.hitpoints > 0 and counter > 0:  #hitpoints init in Player
            for episode in self.game_data:
                counter = counter - 1
                self.run_episode(episode) #load data
                #print ("counter",counter)
        if counter > 0:
            outcome = "Game Over! You lose!"
        else: 
            outcome = "Congratulations! You win!"
        self.end_game(outcome)    


    def end_game(self, outcome):
        ut.slow_print(outcome)
        play_again = input("Would you like to play again? (y/N) ")
        if play_again.lower() == "y":
            start_game()
        else:
            print("Thanks for playing! Goodbye!")
            time.sleep(2)
            raise SystemExit
    
    #run a single episode
    def run_episode(self, episode):
        active_episode = Episode.Episode(episode)
        active_episode.describe_room()
    
        active_treasure = input("Do you want to search for treasure?")
        if active_treasure.lower() == "y":
            treasure_or_hitpoint_change = active_episode.get_treasure()
            #if trap then there could still be treasure
            if type(treasure_or_hitpoint_change) is int:
                self.player.modify_hitpoints(treasure_or_hitpoint_change)
                ut.slow_print("Hitpoints: {}".format(self.player.hitpoints))
                active_treasure = input("Do you want to search for treasure?")
                if active_treasure.lower() == "y":
                    self.player.add_item(treasure_or_hitpoint_change)
                    ut.slow_print("Knapsack:" + self.player.knapsack)
            else:
                self.player.add_item(treasure_or_hitpoint_change)
                ut.slow_print("Knapsack:" + self.player.knapsack)
        else:
            #go to creature


