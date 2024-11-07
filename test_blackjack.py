from unittest import TestCase, main
from unittest.mock import patch
from test_helper2 import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_blackjack(self, input_mock, randint_mock):
        '''
        The user wins by having a blackjack and the dealer has a hand value
        less than 21. 
        '''
        output1 = run_test([8, 1, 2], ['y'], [3, 5, 10], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew an Ace\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        '''
        The user wins by blackjack and again, dealer has hand value less than 21
        Here we are also checking if dealer stops after hitting 17
        '''                   
        output2 = run_test([6, 5, 3, 4, 3], ['y','y','y'], [2, 2, 5, 3, 5], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 2\n" \
                   "Dealer has 4.\n" \
                   "Drew a 5\n" \
                   "Dealer has 9.\n" \
                   "Drew a 3\n" \
                   "Dealer has 12.\n" \
                   "Drew a 5\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        '''
        The user wins by blackjack and again, dealer has hand value less than 21
        This time though, the user instantly hits blackjack and the dealer instantly hits
        a value greater than or equal to 17. This will be a short game.
        Here, we also test how King, Queen and Jack work in the game.
        '''                   
        output3 = run_test([13,1], [], [11,2,7], randint_mock, input_mock)
        expected3 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 2\n" \
                   "Dealer has 12.\n" \
                   "Drew a 7\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)
        self.assertEqual(output3, expected3)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_by_blackjack(self, input_mock, randint_mock):
        '''
        The dealer wins by having a blackjack and the user stops at a hand value
        less than 21. 
        '''
        output1 = run_test([12, 4, 2, 3], ['y','y','n'], [6, 11, 5], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 4\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a Jack\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The dealer wins by blackjack and again, user has hand value less than 21
        This time though, the dealer instantly hits blackjack and the user also exits
        earlier in the game. This will be a short game.
        '''                   
        output2 = run_test([12,7], ['n'], [1,13], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)
        

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_hand_value(self, input_mock, randint_mock):
        '''
        The user wins by having a higher hand value than the dealer.
        '''
        output1 = run_test([7, 6, 5], ['y','n'], [4, 4, 9], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 6\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 4\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        '''
        The user wins again, but this time the dealer exceeds a hand value of 17.
        '''                   
        output2 = run_test([13, 12], ['n'], [8, 7, 4], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 7\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_by_hand_value(self, input_mock, randint_mock):
        '''
        The dealer wins by having a higher hand value than the user.
        Something I discovered is that the dealer will continue to play even if 
        they have won. 
        Lets say final user hand = 13 and dealer gets 15. Even though the dealer has
        won, it will continue drawing cards until it reaches or exceeds 17.
        '''
        output1 = run_test([3,3,7], ['y','n'], [3, 7, 5, 2], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 3\n" \
                   "You have 6. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 13. Hit (y/n)? n\n" \
                   "Final hand: 13.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 7\n" \
                   "Dealer has 10.\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 2\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The user wins again, but this time the dealer exceeds a hand value of 17.
        '''                   
        output2 = run_test([13, 12], ['n'], [8, 7, 4], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 7\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_bust(self, input_mock, randint_mock):
        '''
        The user wins without a blackjack or a hand value greater than dealer.
        The user wins because the dealer busts.
        '''
        output1 = run_test([12,2,7], ['y','n'], [8, 8, 7], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 2\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew an 8\n" \
                   "Dealer has 16.\n" \
                   "Drew a 7\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        '''
        The dealer just gets unlucky in this case. The user decides to quit prematurely,
        however the dealer still loses by drawing a high card and busts.
        The dealer already has a higher hand in their first two draws, but they need to
        draw until they reach or exceed 17, which causes them to lose.
        '''                   
        output2 = run_test([2, 2, 4, 3], ['y','y','n'], [5, 12, 1], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 2\n" \
                   "You have 4. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 11. Hit (y/n)? n\n" \
                   "Final hand: 11.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a Queen\n" \
                   "Dealer has 15.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        '''
        The user wins because the dealer busts. But this time the user has a blackjack
        as well.
        '''                   
        output3 = run_test([4, 8, 9], ['y'], [4, 11, 1], randint_mock, input_mock)
        expected3 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew an 8\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a Jack\n" \
                   "Dealer has 14.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)
        self.assertEqual(output3, expected3)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_by_bust(self, input_mock, randint_mock):
        '''
        The dealer wins without a blackjack or a hand value greater than user.
        The dealer wins because the user busts and the dealer doesnt.
        '''
        output1 = run_test([8,7,7], ['y'], [2, 11, 6], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 7\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "Dealer has 12.\n" \
                   "Drew a 6\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The dealer wins again but this time both the user and dealer are bust.
        However, since the user busts, the dealer will still win regardless.
        The user has a higher hand value even during bust, but still the dealer wins.
        '''                   
        output2 = run_test([7, 12, 1], ['y'], [13, 6, 8], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a Queen\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 28.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew an 8\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The dealer wins again but this time both the user and dealer are bust.
        Now, the dealer has a higher hand value than the user but still wins.
        '''                   
        output3 = run_test([6, 13, 2, 4], ['y','y'], [13, 5, 1], randint_mock, input_mock)
        expected3 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a King\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The dealer wins again but this time both the user and dealer are bust.
        Now, the dealer has a hand value equal to the user
        '''                   
        output4 = run_test([6, 13, 2, 4], ['y','y'], [13, 5, 7], randint_mock, input_mock)
        expected4 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a King\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 7\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        '''
        The dealer wins again but this the dealer has blackjack and the user busts.
        '''                   
        output5 = run_test([1, 1], [], [8, 3, 12], randint_mock, input_mock)
        expected5 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 3\n" \
                   "Dealer has 11.\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)
        self.assertEqual(output3, expected3)
        self.assertEqual(output4, expected4)
        self.assertEqual(output5, expected5)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push(self, input_mock, randint_mock):
        '''
        The dealer and user both have the same hand value (that is not bust or blackjack)
        Thus the game is a draw i.e push
        '''
        output1 = run_test([2,5,6,4,2], ['y','y','y','n'], [5, 6, 8], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew an 8\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

        '''
        Its still a push however the push happens very fast (with the dealer's starting
        hand)
        '''                   
        output2 = run_test([12, 13], ['n'], [13, 11], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a King\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Jack\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

        '''
        Its still a push however both the dealer and user have blackjacks
        '''                   
        output3 = run_test([4, 4, 5, 8], ['y','y'], [3, 3, 6, 9], randint_mock, input_mock)
        expected3 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 4\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 3\n" \
                   "Dealer has 6.\n" \
                   "Drew a 6\n" \
                   "Dealer has 12.\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)
        self.assertEqual(output3, expected3)   


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_typo(self, input_mock, randint_mock):
        '''
        Here we are testing what happens when user enters something else instead of a y/n
        '''
        output1 = run_test([2,5,6,4,2], ['yes','y','y','y','n'], [5, 6, 8], randint_mock, input_mock)
        expected1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "You have 7. Hit (y/n)? yes\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew an 8\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

        '''
        The user now has two typos but the program should work as expected
        '''                   
        output2 = run_test([12, 13], ['no','nooo','n'], [13, 11], randint_mock, input_mock)
        expected2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a King\n" \
                   "You have 20. Hit (y/n)? no\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 20. Hit (y/n)? nooo\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Jack\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"

        self.assertEqual(output1, expected1)
        self.assertEqual(output2, expected2)

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()