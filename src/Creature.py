import Utils as ut

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
        if self.temperment < 10:
            self.temperment += 1
        else:
            self.is_hostile = True

    def describe(self):
        self.speak(self.introduction)

    def greet(self):
        fmap = {"name": self.name, "greeting": self.greeting}
        greeting = "Hello, traveller. My name is {name}! {greeting}".format_map(fmap)
        self.speak(greeting)        
        
    def tell_story(self):
        self.speak(self.story)
    
    def offer_challenge(self, challenge):
        while True:
            if self.is_hostile:
                self.speak("GRAAAAH!!!!! YOU'RE MAKING ME SO MAD!!!")
                break
            else:
                self.outcome = challenge()
                if self.outcome:
                    self.speak("Wow! Great work! You pass!")
                    break
                else:
                    self.make_hostile()
        return self.outcome





