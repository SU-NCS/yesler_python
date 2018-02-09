import unittest
import io
import sys
from Creature import Creature

class CreatureTest(unittest.TestCase):
    def challenge():
        guess = None
        num = randint(1, 10)
        while guess != num:
            guess = input("Give me a number between 1 and 10")
            try:
                guess = int(guess)
                if guess < num:
                    print("Try higher")
                elif guess > num:
                    print("Try lower")
            except:
                print("That was not a number. Try again")
        return True

    def setUp(self):
        self.name = "Max"
        self.intro = "Max is a huge beast with claws."
        self.greeting = "I like long walks on the beach"
        self.story = "I've been walking a long time. Now I want to offer weary travellers challenges."
        self.monster = Creature(self.name, self.intro, self.greeting, self.story)

    def test_monster_can_speak(self):
        words = "This is something to say."
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.speak(words)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), words)

    # def test_monster_can_describe_self(self):
    #     self.assertEqual(self.monster.describe(), "Max is a huge beast with claws.")

    # def test_monster_can_greet_player(self):
    #     dialogue = "Hello, traveller. My name is Max!"
    #     dialogue += self.greeting
    #     self.assertEqual(self.monster.greet(), dialogue)
     
    # def test_if_monster_can_offer_challenge(self):
    #     output = self.monster.offer_challenge(self.challenge)
    #     self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()