from state_machine import state_machine
from events import *

class TennisMachine():
    """a deterministic finite state automaton for Tennis scoring."""
    def __init__(self):
        self.event_store = []

    def event(self, e):
        self.event_store.append(e)
        return len(self.event_store)

    def state(self, events=None, current_state=(0,0)):
        if events is None:
            events = self.event_store

        if GAME_TO_PLAYER_ONE in state_machine[current_state]:
            return state_machine[current_state][GAME_TO_PLAYER_ONE]
        if GAME_TO_PLAYER_TWO in state_machine[current_state]:
            return state_machine[current_state][GAME_TO_PLAYER_TWO]
        if events == []:
            return current_state

        event = events[0]
        new_state = state_machine[current_state][event]
        events = events[1:]

        return self.state(events, new_state)
