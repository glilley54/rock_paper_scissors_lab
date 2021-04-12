from src.game import *
import unittest
from src.player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Sheldon", "Paper")
        self.player_2 = Player("Amy", "Scissors")
        self.player_3 = Player("Gordon", "Rock")
        self.player_4 = Player("John", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Sheldon",self.player_1.name)

    def test_if_the_player_has_a_gesture(self):
        self.assertEqual("Paper", self.player_1.gesture)

    def test_if_rock_and_scissors(self):
        self.assertEqual("Rock wins against scissors.", game(self.player_2.gesture, self.player_3.gesture))

    def test_if_both_gestures_are_the_same(self):
        self.assertEqual("Gestures match! try again!", game(self.player_4.gesture, self.player_3.gesture))
