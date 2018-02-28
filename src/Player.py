import Utils as ut

class Player(object):

    def __init__(self, name=None):
        if not name:
            name = input("What is your name?")
        self.name = name
        self.hitpoints = 10
        self.knapsack = []

    def set_name(self, name):
        self.name = name
    

    def add_item(self, item):
        if len(self.knapsack) < 5:
            self.knapsack.append(item)
        else:
            ut.slow_print("I'm sorry, you must drop an item.")
            
    
    def remove_item(self, item_index=None):
        if item_index == None:
            ut.slow_print("Which item would you like to remove?")
            count = 1
            for item in self.knapsack:
                ut.slow_print(" " + str(count) + ": " + item)
                count += 1
            item_index = input("")    
        if not isinstance(item_index, int):
            item_index = int(item_index)
        try:
            del self.knapsack[item_index - 1]
        except IndexError:
            print("Sorry, no item at this index.")

    # def add_item(self, item):
    #     if len(self.knapsack < 5):
    #         self.knapsack.append(item)
    #     else:
    #         ut.slow_print("I'm sorry, you must drop an item.")
    #         drop = input("Do you want to do this? (y/N)")
    #         if drop.lower() == "y":
    #             ut.slow_print("Which item?")
    #             remove_item()
    #             add_item(item)
    
    # def remove_item(self):
    #     count = 0
    #     for item in self.knapsack:
    #         count += 1
    #         item = str(count) + ". " + item
    #         ut.slow_print(item)
    #     choice = int(input("Enter a number")) - 1
    #         if choice < int(self.knapsack):
    #             del self.knapsack[choice]

            