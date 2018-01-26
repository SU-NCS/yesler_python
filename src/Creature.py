import Utils as ut

class Creature(object):
    """class for creatures that player will encounter."""
    def __init__(self, name, introduction, greeting, story, pace=0.1):
        self.name = name
        self.introduction = introduction
        self.greeting = greeting
        self.story = story
        self.talking_pace = pace

    def introduce(self):
        """Prints out the introduction to the screen."""
        count = 0
        lines = self.introduction.split(".")
        for line in lines:
            line = line.strip()
            line = line + ". "
            ut.slow_print(line)
            count += 1
            if count < len(lines):
                print()    

    def offer_challenge(self, challenge):
        while True:
            outcome = challenge()
            if outcome:
                break
        return outcome



