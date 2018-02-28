import unittest
from unittest import mock
import io
import sys
from Player import Player 

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.name = "Johnny"
        self.player = Player(self.name)

    def test_play_can_reset_name(self):
        name = "Jimmy"
        self.player.set_name(name)
        self.assertEqual(self.player.name, name)

    def test_can_add_to_knapsack(self):
        old_k = self.player.knapsack[:]
        self.player.add_item("screwdriver")
        new_k = self.player.knapsack
        self.assertGreater(len(new_k), len(old_k))

    def test_can_add_no_more_than_five_items(self):
        for i in range(0,6):
            self.player.add_item("blah")
        knap = self.player.knapsack
        self.assertLessEqual(len(knap), 5)
    
    def test_remove_item(self):
        self.player.knapsack = []
        self.player.add_item("wrench")
        self.player.add_item("screwdriver")
        with mock.patch('builtins.input',side_effect='1'):
            output = io.StringIO()
            sys.stdout = output
            self.player.remove_item()
            sys.stdout = sys.__stdout__
            self.assertEqual(output.getvalue(), "Which item would you like to remove? 1: wrench 2: screwdriver")

    def test_can_add_items_after_five_if_remove_one(self):
        self.player.knapsack = []
        for i in range(0,5):
            self.player.add_item("blah")
        output = io.StringIO()
        sys.stdout = output
        self.player.add_item("last_blah")
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "I'm sorry, you must drop an item.")

if __name__ == '__main__':
    unittest.main()        