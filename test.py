import unittest
from tennis import TennisMachine
from events import *

class TennisGameTests(unittest.TestCase):
    def test_initial_state(self):
        tennis = TennisMachine()
        self.assertEqual(tennis.game_state(), (0,0))

    def test_player_one_can_score(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.game_state()
        self.assertEqual(score, (1,0))

    def test_player_one_can_score_twice(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.game_state()
        self.assertEqual(score, (2,0))

    def test_player_one_can_win_and_game_resets(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.game_state()
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
        score = tennis.game_state()
        self.assertEqual(score, (3,3))

class TennisSetTests(unittest.TestCase):
    def test_can_count_a_set(self):
        tennis = TennisMachine()
        self.assertEqual(tennis.set_state(), (0,0))

    def test_can_win_a_set(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        score = tennis.set_state()
        self.assertEqual(score, (1,0))

    def test_can_win_one_set_each(self):
        tennis = TennisMachine()
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_ONE_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        tennis.event(PLAYER_TWO_SCORED)
        score = tennis.set_state()
        self.assertEqual(score, (1,1))

    def test_can_win_six_sets_each(self):
        tennis = TennisMachine()
        for i in range(6):
            tennis.event(PLAYER_ONE_SCORED)
            tennis.event(PLAYER_ONE_SCORED)
            tennis.event(PLAYER_ONE_SCORED)
            tennis.event(PLAYER_ONE_SCORED)
            tennis.event(PLAYER_TWO_SCORED)
            tennis.event(PLAYER_TWO_SCORED)
            tennis.event(PLAYER_TWO_SCORED)
            tennis.event(PLAYER_TWO_SCORED)
        score = tennis.set_state()
        self.assertEqual(score, (6,6))
