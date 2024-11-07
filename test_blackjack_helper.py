from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.

  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name,1),'Drew an Ace\n')
    self.assertEqual(get_print(print_card_name,8),'Drew an 8\n')
    self.assertEqual(get_print(print_card_name,3),'Drew a 3\n')
    self.assertEqual(get_print(print_card_name,5),'Drew a 5\n')
    self.assertEqual(get_print(print_card_name,11),'Drew a Jack\n')
    self.assertEqual(get_print(print_card_name,12),'Drew a Queen\n')
    self.assertEqual(get_print(print_card_name,13),'Drew a King\n')
    self.assertEqual(get_print(print_card_name,0),'BAD CARD\n')
    self.assertEqual(get_print(print_card_name,-3),'BAD CARD\n')
    self.assertEqual(get_print(print_card_name,15),'BAD CARD\n')

  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card),11)
    self.assertEqual(mock_random([11], draw_card),10)
    self.assertEqual(mock_random([12], draw_card),10)
    self.assertEqual(mock_random([13], draw_card),10)
    self.assertEqual(mock_random([4], draw_card),4)
    self.assertEqual(mock_random([9], draw_card),9)
    self.assertEqual(mock_random([-1], draw_card),-1) #might not be important as the range of the randint is just 1-13
    self.assertEqual(mock_random([0], draw_card),0)

  def test_print_header(self):
    self.assertEqual(get_print(print_header,"YOUR TURN"),"-----------\nYOUR TURN\n-----------\n")
    self.assertEqual(get_print(print_header,"DEALER TURN"),"-----------\nDEALER TURN\n-----------\n")
    self.assertEqual(get_print(print_header,"GAME RESULT"),"-----------\nGAME RESULT\n-----------\n")
    self.assertEqual(get_print(print_header,""),"-----------\n\n-----------\n")
    self.assertEqual(get_print(print_header,333),"-----------\n333\n-----------\n")
    self.assertEqual(get_print(print_header,333.00),"-----------\n333.0\n-----------\n")
    self.assertEqual(get_print(print_header,333.0001),"-----------\n333.0001\n-----------\n")
    self.assertEqual(get_print(print_header,"ViSioN"),"-----------\nViSioN\n-----------\n")

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([3,4], draw_starting_hand, "YOUR"),7)
    self.assertEqual(mock_random([11,6], draw_starting_hand, "DEALER"),16)
    self.assertEqual(mock_random([12,8], draw_starting_hand, "DEALER"),18)
    self.assertEqual(mock_random([10,13], draw_starting_hand, "DEALER"),20)
    self.assertEqual(mock_random([1,1], draw_starting_hand, "YOUR"),22)
    self.assertEqual(mock_random([13,13], draw_starting_hand, "DEALER"),20)
    self.assertEqual(mock_random([-10,11], draw_starting_hand, "DEALER"),0) #just checking
    self.assertEqual(mock_random([0,0], draw_starting_hand, "YOUR"),0)
    self.assertEqual(mock_random([-1,0], draw_starting_hand, "YOUR"),-1)
    self.assertEqual(mock_random([0,-3], draw_starting_hand, "YOUR"),-3)
    self.assertEqual(mock_random([15,14], draw_starting_hand, "DEALER"),29)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status,10),"Final hand: 10.\n")
    self.assertEqual(get_print(print_end_turn_status,15),"Final hand: 15.\n")
    self.assertEqual(get_print(print_end_turn_status,6),"Final hand: 6.\n")
    self.assertEqual(get_print(print_end_turn_status,21),"Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status,25),"Final hand: 25.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status,30),"Final hand: 30.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status,0),"Final hand: 0.\n")
    self.assertEqual(get_print(print_end_turn_status,-333),"Final hand: -333.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status,18,21),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,9,11),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,21,15),'-----------\nGAME RESULT\n-----------\nYou win!\n')
    self.assertEqual(get_print(print_end_game_status,7,6),'-----------\nGAME RESULT\n-----------\nYou win!\n')
    self.assertEqual(get_print(print_end_game_status,25,16),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,11,26),'-----------\nGAME RESULT\n-----------\nYou win!\n')
    self.assertEqual(get_print(print_end_game_status,30,30),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,15,15),'-----------\nGAME RESULT\n-----------\nPush.\n')
    self.assertEqual(get_print(print_end_game_status,21,21),'-----------\nGAME RESULT\n-----------\nPush.\n')
    self.assertEqual(get_print(print_end_game_status,0,0),'-----------\nGAME RESULT\n-----------\nPush.\n')
    self.assertEqual(get_print(print_end_game_status,-1,1),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')
    self.assertEqual(get_print(print_end_game_status,-333,-333),'-----------\nGAME RESULT\n-----------\nPush.\n')
    self.assertEqual(get_print(print_end_game_status,34,34),'-----------\nGAME RESULT\n-----------\nDealer wins!\n')


if __name__ == '__main__':
    unittest.main()