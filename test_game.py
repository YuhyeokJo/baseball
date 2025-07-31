from game import Game
import pytest


def test_exception_when_input_is_none():
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)
