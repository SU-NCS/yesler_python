import Utils as ut
from random import *

class Creature(object):
    """Class for creatures that player will encounter."""
    outcome = False
    temperment = 0
    is_hostile = False

    def __init__(self, name, introduction, greeting=None, story=None, 
                pace=0.1):
        self.name = name
        self.introduction = introduction
        self.greeting = greeting
        self.story = story
        self.pace = pace

    def speak(self, dialog):
        """Prints out text to the screen if creature is not hostile."""
        if self.is_hostile or not dialog:
            ut.slow_print("I don't have anything to say to you.")
            self.offer_challenge()
        else:
            if len(dialog) > 80:
                for line in dialog.split("."):
                    line = line.strip()
                    line = line + ". "
                    ut.slow_print(line, self.pace)
            else:
                ut.slow_print(dialog, self.pace)

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
        if self.is_hostile:
            ut.slow_print("GRAAAAH!!!! YOU'RE MAKING ME SO MAD!!!!")
            return False
        ut.slow_print("Ah! So you want a challenge! Here you go!", 
                        self.pace)
        while True:
            if self.is_hostile:
                break 
            self.outcome = challenge()
            if self.outcome:
                break
            else:
                self.make_hostile()
        return self.outcome




