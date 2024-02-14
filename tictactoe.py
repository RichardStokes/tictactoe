class TicTacToeGame:

	def __init__(self):
		rows, cols = (3,3)
		self.board = [['-' for i in range(cols)] for j in range(rows)]
		self.player_1 = True
		self.game_over = False

	def mark_square(self,x,y, mark):
		try:
			if self.board[x][y] == '-':
				self.board[x][y] = mark
				return True
			else:
				print("Square not empty! Please pick another square:")
				return False
		except IndexError as e:
			print("<!> ERROR: Coordinates must be in the range 0-2 <!>")
		except ValueError as e:
			print("<!> ERROR: coordinates must be space-delimited integer values <!>")

	
	def __str__(self):
		str = "\n"
		for row in self.board:
			x = ""
			for cell in row:
				x += (f"{cell}   ")
			str += x.strip() + "\n"
		return str
		
	
	def prompt_for_coordinates(self):
		coord_string = input("Please enter the desired square:").split()
		try:
			coords = [int(n) for n in coord_string]
			return coords
		except ValueError as e:
			print("<!> ERROR: coordinates must be space-delimited integer values <!>")

	def start_game(self):
		print("""Welcome to Tic Tac Toe!
			Player 1, please start!:""")
		print(self)
		while not self.game_over:
			mark = 'X' if self.player_1 else '0'
			marked = False
			while not marked:
				coords = None
				while coords == None:
					coords = self.prompt_for_coordinates()
				marked = self.mark_square(*coords, mark)
			print(self)
			if self.winning_condition(*coords, mark):
				self.game_over = True
				print("Congratulations, you won!")
			elif self.board_full():
				self.game_over = True
				print("The game is tied!")
			else:
				self.player_1 = not self.player_1

	def winning_condition(self, x, y, mark, previous_coords=None):
		if previous_coords:
			x_direction = x - previous_coords[0]
			y_direction = y - previous_coords[1]

			x += x_direction
			y += y_direction

			if self.valid_coordinates(x,y) and self.board[x][y] == mark:
				return True 
		else:
			adj_coords = self.adjacent_coordinates(x,y)

			# Loop through the adjacent squares, checking for a matching mark	
			for coords in adj_coords:
				i, j = coords
				if self.board[i][j] == mark:
					return self.winning_condition(*coords, mark, previous_coords=(x,y))
		return False

	# Find a list of all squares adjacent to a certain square
	def adjacent_coordinates(self,x,y):
		coords = []
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if self.valid_coordinates(i,j) and (i, j) != (x, y):
					coords.append((i, j))
		return coords
	
	def board_full(self):
		for i in self.board:
			for j in i:
				if j == "-":
					return False
		return True
	
	def valid_coordinates(self, *coords):
		x,y = coords
		valid = True if x in range(3) and y in range(3) else False
		return valid


if __name__ == '__main__':
	game = TicTacToeGame()
	game.start_game()
	