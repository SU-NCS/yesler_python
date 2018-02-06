import Utils as ut

class Creature(object):
    """class for creatures that player will encounter."""
    def __init__(self, name, introduction, greeting=None, story=None, 
                pace=0.1, is_hostile = False):
        self.name = name
        self.introduction = introduction
        self.greeting = greeting
        self.story = story
        self.pace = pace
        self.is_hostile = is_hostile
        self.temperment = 0
        if is_hostile:
            self.temperment = 10

    def speak(self, dialog):
        """Prints out text to the screen if creature is not hostile."""
        if self.is_hostile or not dialog:
            ut.slow_print("I don't have anything to say to you.")
            self.offer_challenge()
        else:
            for line in dialog.split("."):
                line = line.strip()
                line = line + ". "
                ut.slow_print(line, self.pace)
    
    def make_hostile(self):
        if self.temperment < 10:
            self.temperment += 1
        else:
            self.is_hostile = True

    def describe(self):
        self.speak(self.introduction)

    def greet(self):
        ut.slow_print("Hello, traveller. My name is %s!" % self.name, self.pace)
        self.speak(self.greeting)        
        
    def tell_story(self):
        self.speak(self.story)
    
    def offer_challenge(self, challenge=None):
        if self.is_hostile or not challenge:
            return False
        
        ut.slow_print("Ah! So you want a challenge! Here you go!", 
                        self.pace)
        while True:
            outcome = challenge()
            if outcome:
                break
            else:
                self.make_hostile()
        return outcome

    


