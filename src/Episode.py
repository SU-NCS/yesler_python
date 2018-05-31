import Utils as ut

class Episode(object):
    """
    Class manages one episode or room of the adventure game.
    Pre-conditions: Must have episode data as a dictionary.
    PROCESS: Methods to describe room, continue the narrative,
    and get treasure.
    """
    def __init__(self, episode_data):
        """ Initialize the episode data. Input dictionary."""
        # Initialize episode properties
        self.room_description = episode_data['room_description']
        self.episode_narrative = episode_data['episode_narrative']
        self.treasure = episode_data['treasure']
        self.traps = episode_data['traps']
        # Set hitpoint change for traps or treasure
        self.hitpoint_change = episode_data['hitpoint_change']
    

    def describe_room(self):
        """Describes the room using slow print function."""
        try:
            ut.slow_print(self.room_description)
        except Exception as e:
            print("Something went wrong: " + e)
        
    def print_narrative(self):
        """Prints any episode narrative that's included."""
        if self.episode_narrative:
            ut.slow_print(self.episode_narrative)
        

    def get_treasure(self):
        """ Searches room for treasure. 
        Return TUPLE:
        first value is hitpoint change, second value is treausre, and third is whether we can try again."""
        try_again = True
        hitpoints = 0
        treasure = None
        while try_again: # Try until we go through all the choices.
            if self.traps: # Spring traps
                ut.slow_print(self.traps)
                self.traps = None 
                hitpoints = self.hitpoint_change
                reply = input("Would you like to search again? (Y/n)")
                if reply.lower() == "n":
                    try_again = False
            elif self.treasure:
                ut.slow_print("You found treasure! {}".format(self.treasure))
                treasure = self.treasure
                try_again = False
            else:
                try_again = False
        
        return (hitpoints, treasure)

        # # If there's traps, spring trap.
        # if self.traps:
        #     ut.slow_print(self.traps)
        #     #self.hitpoints = self.hitpoints + self.hitpoint_change  #use hitpoints if you there is trap in the way
        #     #ut.slow_print("Your hitpoints: {}".format(self.hitpoints))
        #     self.traps = None
        #     if self.treasure:
        #         try_again = True
        #     return (self.hitpoint_change, None, try_again)
        # elif self.treasure:
        #     treasure = "You found treasure! Hooray! " + self.treasure
        #     ut.slow_print(treasure)
        #     return (self.hitpoint_change, self.treasure, try_again)

    # REMOVED METHOD. Manage creature outside of episode.
    # def talk_to_creature(self):
    #  
    #     self.creature.greet()
    #     more = input("Do you want to hear more? (Y/n)")
    #     if more.lower()
    #     self.creature.describe()
    #     self.creature.tell_story()
    #     self.creature.offer_challenge(self.challenge)

            


    




