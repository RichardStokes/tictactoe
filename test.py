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
			- | - | -
			-+--+--+-
			- | - | -
			-+--+--+-
			- | - | -
"""
        self.assertMultiLineEqual(initial_state, x, "The board hasn't printed correctly.")
    

    def test_adjacent_coordinates(self):
        middle_coords = (1,1)
        adjacent_coords = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)].sort()
        self.assertEqual(adjacent_coords, self.game.adjacent_coordinates(*middle_coords).sort())

        corner_coords = (2,2)
        adjacent_coords = [(2,1), (1,1), (1,2)].sort()
        self.assertEqual(adjacent_coords, self.game.adjacent_coordinates(*corner_coords).sort())

    def test_winning_condition(self):
        
        winning_coords = {
            ((0,0), (1,1), (2,2)),  # Diagonal
            ((0,2), (1,1), (2,0)),  # Diagonal
            ((0,0), (0,1), (0,2)),  # Top row
            ((1,0), (1,1), (1,2)),  # Middle row
            ((2,0), (2,1), (2,2)),  # Bottom row
            ((0,0), (1,0), (2,0)),  # Left column
            ((0,1), (1,1), (2,1)),  # Middle column
            ((0,2), (1,2), (2,2))   # Right column
        }


        for coords in winning_coords:
            for c in coords:
                self.game.mark_square(*c, "X")
            last_square = coords[-1] 
            winning = self.game.winning_condition(*last_square, "X")
            self.assertTrue(winning)
            self.game.board = self.game.getCleanBoard()

        not_winning_coords = [(0,0), (1,0), (1,1)]
        for coords in not_winning_coords:
            x, y = coords
            self.game.board[x][y] = "X"
        winning = self.game.winning_condition(1,1, "X")
        self.assertFalse(winning)


    def test_board_full(self):
        for i in range(3):
            for j in range(3):
                self.game.board[i][j] = "X"
        self.assertTrue(self.game.board_full())

    
    def test_valid_coordinates(self):
        self.assertTrue(self.game.valid_coordinates(0,2))
        self.assertFalse(self.game.valid_coordinates(-1, 3))

if __name__ == "__main__":
    unittest.main()
