import unittest
from tictactoe import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToeGame()

    def test_mark_square(self):
        mark = "X"
        marked = self.game.mark_square(0,0, mark)
        self.assertEqual(self.game.board[0][0], mark, "The square is marked incorrectly.")
        mark = "0"
        marked_again = self.game.mark_square(0,0, mark)
        self.assertNotEqual(self.game.board[0][0], mark, "The square has been marked over.")
        self.assertFalse(marked_again)
    
    def test__str__(self):
        x = str(self.game)
        initial_state = """
-   -   -
-   -   -
-   -   -
"""
        self.assertMultiLineEqual(initial_state, x, "The board hasn't printed correctly.")


if __name__ == "__main__":
    unittest.main()
