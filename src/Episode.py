import json
import Utils as ut
import challenges
import Creature

class Episode:
    """
    Class manages one episode or room of the adventure game.
    IN: episode data as a dictionary.
    PROCESS: Methods to describe room, interact with creature,
    and get treasure.
    """
    def __init__(self, episode_data):
        cd = episode_data["creature"]
        self.creature = Creature.Creature(cd['name'], cd['introduction'], cd['greeting'], cd['story'])
        self.room_description = episode_data['room_description']
        #print (self.room_description)
        self.treasure = episode_data['treasure']
        self.traps = episode_data['traps']
        self.hitpoint_change = episode_data['hitpoint_change']
        print("Episode loaded")
    
    def describe_room(self):
        """Describes the room using slow print function."""
        try:
            ut.slow_print(self.room_description)
        except Exception as e:
            print("Something went wrong: " + e)
        
    
    def get_treasure(self):
        """ Searches room for treasure. 
        Return TUPLE:
        first value is hitpoint changet, and whether we can try again."""
        if self.traps and self.treasure:
            ut.slow_print(self.traps)
            #self.hitpoints = self.hitpoints + self.hitpoint_change  #use hitpoints if you there is trap in the way
            #ut.slow_print("Your hitpoints: {}".format(self.hitpoints))
            self.traps = None
            return (self.hitpoint_change, True)
        elif self.treasure:

            return self.treasure


    def talk_to_creature(self):
        self.creature.greet()
        self.creature.describe()
        self.creature.tell_story()
        self.creature.offer_challenge(self.challenge)

            


    




