import json
import time
import os
import Player
import Episode

class Game:

    def __init__(self, story, challenge_path):
        self.player = Player.Player()
        try:
            with open(story) as f:
                self.game_data = json.load(f)
        except Exception as e:
            print("Something went wrong with your file. I need a story: {}".format(e))
        # Import our challenges
        try:
            for root, dirs, files in os.walk(challenge_path):
                __all__ = [name.split(".")[0] for name in files if "challenge" in name]
        except Exception as e2:
            print("There's something wrong with your challenge path: {}".format(e))

    def start_game(self):
        counter = len(self.game_data)
        while self.player.hitpoints > 0:
            for episode in self.game_data:
                counter = counter - 1
                load_episode(episode)
        if counter > 0:
            outcome = "Game Over! You lose!"
        else: 
            outcome = "Congratulations! You win!"
        self.end_game(outcome)    


    def end_game(self, outcome):
        ut.slow_print(outcome)
        play_again = input("Would you like to play again? (y/N) ")
        if lower(play_again) == "y":
            start_game()
        else:
            print("Thanks for playing! Goodbye!")
            time.sleep(2)
            raise SystemExit
    

    def load_episode(self, episode):
        episode = Episode.Episode(episode)
    



