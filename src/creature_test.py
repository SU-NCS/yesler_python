import unittest
import io
import sys
from Creature import Creature
from random import *

class CreatureTest(unittest.TestCase):
    
    def fail_challenge(self):
        return False

    def success_challenge(self):
        return True
    
    def challenge(self):
        guess = None
        num = randint(1, 10)
        for i in range(0, 10):
            guess = input("Give me a number between 1 and 10")
            try:
                guess = int(guess)
                if guess == num:
                    return True
                elif guess < num:
                    print("Try higher")
                elif guess > num:
                    print("Try lower")
            except:
                print("That was not a number. Try again")
        return False

    def setUp(self):
        self.name = "Max"
        self.intro = "Max is a huge beast with claws."
        self.greeting = "I like long walks on the beach"
        self.story = "I've been walking a long time. Now I want to offer weary travellers challenges."
        self.pace = 0.01
        self.monster = Creature(self.name, self.intro, self.greeting, self.story, self.pace)

    def test_monster_can_speak(self):
        words = "This is something to say."
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.speak(words)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), words)

    def test_monster_can_describe_self(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.describe()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), self.intro)

    def test_monster_can_greet(self):
        fmap = {"name": self.name, "greeting": self.greeting}
        expected = "Hello, traveller. My name is {name}! {greeting}".format_map(fmap)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.greet()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)

    def test_monster_can_tell_story(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.tell_story()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), self.story)

    def test_if_monster_can_become_more_hostile(self):
        hostility = self.monster.temperment
        self.monster.make_hostile()
        newhostility = self.monster.temperment
        self.assertTrue(hostility + 1 == newhostility)
    
    def test_monster_is_pissed(self):
        for i in range(0,11):
            self.monster.make_hostile()
            print(self.monster.temperment)
        self.assertTrue(self.monster.is_hostile)

    def test_monster_challenge_succeed(self):
        output = self.monster.offer_challenge(self.success_challenge)
        self.assertTrue(output)
    
    def test_monster_challenge_can_fail(self):
        for i in range(0,10):
            output = self.monster.offer_challenge(self.fail_challenge)
        self.assertFalse(output)

    def test_monster_real_challenge_works(self):
        output = self.monster.offer_challenge(self.challenge)
        self.assertTrue(output)

    def test_monster_challenge_speaks_on_fail(self):
        self.monster.is_hostile = True
        expected_output = "GRAAAAH!!!!! YOU'RE MAKING ME SO MAD!!!"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.offer_challenge(self.fail_challenge)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_monster_challenge_speaks_on_success(self):
        expected_output = "Wow! Great work! You pass!"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monster.offer_challenge(self.success_challenge)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()