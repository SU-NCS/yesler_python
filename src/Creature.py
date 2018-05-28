import Utils as ut

class Creature(object):
    """Class for creatures that player will encounter."""

    def __init__(self, name, introduction, greeting=None, story=None, 
                pace=0.1):
        # Initialize Creature properties.
        self.name = name
        self.introduction = introduction
        self.greeting = greeting
        self.story = story
        self.pace = pace
        self.temperment = 0
        self.is_hostile = False

    def speak(self, dialog):
        """Prints out text to the screen if creature is not hostile."""
        if not dialog:
            ut.slow_print("I don't have anything to say to you.")
        else:
            if len(dialog) > 80:
                output = ""
                for line in dialog.split(" "):
                    if len(output) < 80:
                        output += line
                    else:
                        ut.slow_print(line, self.pace)
                        output = ""
            else:
                ut.slow_print(dialog, self.pace)

    def make_hostile(self):
        """
        Increments hostility until creature is hostile. Episode must be
        restarted if the creature becomes hostile.
        """
        if self.temperment < 10:
            self.temperment += 1
        else:
            self.is_hostile = True

    def describe(self):
        """Creature prints its introduction."""
        self.speak(self.introduction)

    def greet(self):
        """Creature greets player"""
        fmap = {"name": self.name, "greeting": self.greeting}
        greeting = "Hello, traveller. My name is {name}! {greeting}".format_map(fmap)
        self.speak(greeting)        
        
    def tell_story(self):
        """Creature tells a story."""
        self.speak(self.story)
    
    def offer_challenge(self, challenge):
        """Creature takes challenge function and tries the challenge until it returns
        true or the creature becomes hostile."""
        while not self.is_hostile: # As long as the creature isn't hostile, we try the challenge.
            self.outcome = challenge()
            print(self.outcome)
            print(self.temperment)
            if self.outcome:
                return True # if we pass the challenge we win the episode
            else: # Otherwise increase hostility and try again.
                self.make_hostile()
        
        return not self.is_hostile # Creature became too hostile and we fail. 




