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
    

    def test_adjacent_coordinates(self):
        starting_coords = (1,1)
        adjacent_coords = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]
        self.assertEqual(adjacent_coords, self.game.adjacent_coordinates(*starting_coords))


if __name__ == "__main__":
    unittest.main()
