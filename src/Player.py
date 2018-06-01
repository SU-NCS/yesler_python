import Utils as ut

class Player(object):
    """
        Class to manage the player object. This deals with the player's stats,
        their name, and the things they carry.
    """
    name = None 

    def __init__(self):
        """
        Sets the name or prompts for a name. Initializes hit points,
        and creates an empty list for a knapsack.
        """
        self.name = input("What is your name?")
        # self.name = input_name
        self.hitpoints = 10
        self.knapsack = []


    def set_name(self, name):
        """Method to set or reset name. Not necessary if constructor used."""
        self.name = name
    

    def modify_hitpoints(self, points=None):
        """Modify hitpoints. Cannot go past 10 hitpoints. 
        Parameter points is the number of points to change.
        If damage is done, this should be negative."""
        self.hitpoints = self.hitpoints + points
        if self.hitpoints > 10:
            ut.slow_print("Hitpoints already maxed out.")
            self.hitpoints = 10


    def add_item(self, item):
        """Add an item to the knapsack if the knapsack is not full."""
        if len(self.knapsack) < 5: # If the knapsack's not full, just add item.
            self.knapsack.append(item) 
        else: # Otherwise offer to drop.
            ut.slow_print("I'm sorry, you must drop an item. \n Do you want to do this? (y/N)")
            drop = input("")
            if drop.lower() == "y":
                self.remove_item()
                self.knapsack.append(item)
            else:
                ut.slow_print("I guess you don't want this new item that much.")


    def remove_item(self, item_index=None):
        """Method to remove item from knapsack. 
        Input: item_index is the index of the item to remove. Not required.
        """ 
        if item_index == None: #Get item index if none was passed by argument.
            ut.slow_print("Which item would you like to remove?")
            count = 1
            for item in self.knapsack:
                ut.slow_print(" " + str(count) + ": " + item)
                count += 1
            item_index = input("")    
        if not isinstance(item_index, int): # Convert input to integer.
            item_index = int(item_index)
        try: # Try to delete the item. Catch error as needed.
            del self.knapsack[item_index - 1]
        except IndexError:
            print("Sorry, no item at this index.")            