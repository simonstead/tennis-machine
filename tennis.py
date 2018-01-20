from state_machine import state_machine, set_state_machine
from events import *

class TennisMachine():
    """a deterministic finite state automaton for Tennis scoring."""
    def __init__(self):
        self.event_store_for_game = []
        self.event_store_for_set = []
        self.event_store_for_match = []

    def event(self, e):
        self.event_store_for_game.append(e)
        return len(self.event_store_for_game)

    def event_set(self, e):
        self.event_store_for_set.append(e)
        return len(self.event_store_for_set)

    def event_match(self, e):
        self.event_store_for_set.append(e)
        return len(self.event_store_for_match)

    def game_state(self, events=None, current_state=(0,0)):
        if events is None:
            events = self.event_store_for_game

        if GAME_TO_PLAYER_ONE in state_machine[current_state]:
            return state_machine[current_state][GAME_TO_PLAYER_ONE]
        if GAME_TO_PLAYER_TWO in state_machine[current_state]:
            return state_machine[current_state][GAME_TO_PLAYER_TWO]
        if events == []:
            return current_state

        event = events[0]
        new_state = state_machine[current_state][event]
        events = events[1:]

        return self.game_state(events, new_state)

    def set_state(self, events=None, current_state_game=(0,0), current_state_set=(0,0)):
        if events is None:
            events = self.event_store_for_game

        if GAME_TO_PLAYER_ONE in state_machine[current_state_game]:
            current_state_set = set_state_machine[current_state_set][GAME_TO_PLAYER_ONE]
            new_state_game = state_machine[current_state_game][GAME_TO_PLAYER_ONE]
            return self.set_state(events, new_state_game, current_state_set)
        if GAME_TO_PLAYER_TWO in state_machine[current_state_game]:
            current_state_set = set_state_machine[current_state_set][GAME_TO_PLAYER_TWO]
            new_state_game = state_machine[current_state_game][GAME_TO_PLAYER_TWO]
            return self.set_state(events, new_state_game, current_state_set)
        if events == []:
            return current_state_set

        event = events[0]
        new_state_game = state_machine[current_state_game][event]
        events = events[1:]

        return self.set_state(events, new_state_game, current_state_set)
