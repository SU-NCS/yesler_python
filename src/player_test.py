import unittest
from unittest import mock
import io
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
    
    # def test_can_remove_item_from_knapsack(self):
    #     item = "wrench"
    #     self.player.add_item(item)
    #     old_k = self.player.knapsack[:]
    #     i = self.player.knapsack.index(item)
    #     self.player.remove_item(i)
    #     new_k = self.player.knapsack[:]
    #     self.assertLess(len(new_k), len(old_k))

    # def test_can_remove_item_from_knapsack_with_string_parameter(self):
    #     item = "wrench"
    #     self.player.add_item(item)
    #     old_k = self.player.knapsack[:]
    #     i = self.player.knapsack.index(item)
    #     self.player.remove_item(str(i))
    #     new_k = self.player.knapsack[:]
    #     self.assertLess(len(new_k), len(old_k))
    
    def test_remove_item_asks_player_which_item_to_remove(self):
        expected_output = "Which item would you like to remove?"
        count = 0
        for i in range(0,5):
            expected_output += " " + str(count) + ": blah"
            self.player.add_item("blah")
            count += 1
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.player.remove_item()
            received_output = mock_stdout.getvalue()
            self.assertEqual(expected_output, received_output)
    
    
    def test_can_remove_selected_item_from_knapsack(self):
        mock_array = ["wrench", "flashlight", "candy"]
        for item in mock_array:
            self.player.add_item(item)
        self.player.remove_item()
        expected_output = ["wrench", "candy"]
        self.assertEqual(self.player.knapsack, expected_output)


if __name__ == '__main__':
    unittest.main()        