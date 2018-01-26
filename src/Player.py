import Utils as ut

class Player(object):

    def __init__(self, name=None):
        if not name:
            name = input("What is your name?")
        self.name = name
        self.knapsack = []

    def set_name(self, name):
        self.name = name
    

    def add_item(self, item):
        if len(self.knapsack < 5):
            self.knapsack.append(item)
        else:
            ut.slow_print("I'm sorry, you must drop an item.")
            drop = input("Do you want to do this? (y/N)")
            if drop.lower() == "y":
                ut.slow_print("Which item?")
                remove_item()
                add_item(item)
    
    def remove_item(self):
        count = 0
        for item in self.knapsack:
            count += 1
            item = str(count) + ". " + item
            ut.slow_print(item)
        choice = int(input("Enter a number")) - 1
            if choice < int(self.knapsack):
                del self.knapsack[choice]

            