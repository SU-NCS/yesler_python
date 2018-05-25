import json
import Utils as ut
import Creature

class Episode:
#figure out how to pass a challenge into the creature.
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
        try:
            ut.slow_print(self.room_description)
        except Exception as e:
            print("Something went wrong: " + e)
        
    
    def get_treasure(self):
        if self.traps:
            ut.slow_print(self.traps)
            #self.hitpoints = self.hitpoints + self.hitpoint_change  #use hitpoints if you there is trap in the way
            #ut.slow_print("Your hitpoints: {}".format(self.hitpoints))
            self.traps = None
            return self.hitpoint_change
        elif self.treasure:
            temp = self.treasure
            self.treasure = None
            return temp
        else:
            return False

    def talk_to_creature(self):
        self.creature.greet()
        self.creature.describe()
        self.creature.tell_story()
        self.creature.offer_challenge(self.challenge)
        


    




