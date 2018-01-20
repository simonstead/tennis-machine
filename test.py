import unittest
from tennis import TennisMachine
from events import *

class Tennis(unittest.TestCase):
    def test_initial_state(self):
        tennis = TennisMachine()
        self.assertEqual(tennis.state(), (0,0))

    def test_player_one_can_score(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.state()
        self.assertEqual(score, (1,0))

    def test_player_one_can_score_twice(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.state()
        self.assertEqual(score, (2,0))

    def test_player_one_can_win_and_game_resets(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.state()
        self.assertEqual(score, (0,0))

    def test_can_deuce_advantage_deuce(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        score = tennis.state()
        self.assertEqual(score, (3,3))
