import Utils as ut

class Creature(object):
    """Class for creatures that player will encounter."""

    def __init__(self, creature_data, pace=0.1):
        # Initialize Creature properties.
        self.name = creature_data['name']
        self.introduction = creature_data['introduction']
        self.greeting = creature_data['greeting']
        self.story = creature_data['story']
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
        self.speak("You're making me so mad!")
        if self.temperment < 5:
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
        # We try the challenge.
        outcome = challenge.guess()
        if not outcome:
            self.make_hostile() # if challenge failed make more hostile
        return outcome # Return the outcome of the challenge
        



