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

    def test_player_can_lose_hit_points(self):
        self.player.modify_hitpoints(-1)
        self.assertEqual(9, self.player.hitpoints)

    def test_player_can_gain_hitpoints(self):
        self.player.hitpoints = 5
        self.player.modify_hitpoints(2)
        self.assertEqual(7, self.player.hitpoints)

    def test_player_can_max_hitpoints(self):
        self.player.modify_hitpoints(2)
        self.assertEqual(10, self.player.hitpoints)

    def test_can_add_to_knapsack(self):
        old_k = self.player.knapsack[:]
        self.player.add_item("screwdriver")
        new_k = self.player.knapsack
        self.assertGreater(len(new_k), len(old_k))
    
    def test_remove_item(self):
        self.player.knapsack = []
        self.player.add_item("wrench")
        with mock.patch('builtins.input', side_effect='1'):
            output = io.StringIO()
            sys.stdout = output
            self.player.remove_item()
            sys.stdout = sys.__stdout__
            self.assertEqual(output.getvalue(), "Which item would you like to remove? 1: wrench")

    def test_can_remove_item_if_extra_items(self):
        self.player.knapsack = []
        for i in range(0,5):
            self.player.add_item("blah")
        with mock.patch('builtins.input', side_effect=['y', 5]):
            output = io.StringIO()
            sys.stdout = output 
            self.player.add_item("last_blah")
            sys.stdout = sys.__stdout__
            self.assertEqual(self.player.knapsack, ['blah', 'blah', 'blah', 'blah', 'last_blah'])
            

if __name__ == '__main__':
    unittest.main()        