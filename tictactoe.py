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
			self.player_1 = not self.player_1

	def winning_condition(self, x, y, mark, previous_coords=None):
		adj_coords = self.adjacent_coordinates(x,y)

		# Remove the previous square from any possible path forward
		if previous_coords in adj_coords:
			adj_coords.remove(previous_coords)

		# if from_same_row(prev_coords):
		#	search_same_row
		# elsif from_same_col(prev_coords):
		#	search_same_col(prev_coords):
		# elsif from_diag(prev_coords):
		#	search_next_diag

		# Loop through the adjacent squares, checking for a matching mark	
		for coords in adj_coords:
			i, j = coords
			try:
				if self.board[i][j] == mark:
					if not previous_coords:
						return self.winning_condition(*coords, mark, previous_coords=(x,y))
					else:
						if i == previous_coords[0]:
							direction = j - previous_coords[j]
							if self.board[i][j + direction]:
								return True
						elif j == previous_coords[1]:
							direction = i - previous_coords[i]
							if self.board[i+direction][j]:
								return True
						else:
							i_direction = i - previous_coords[0]
							j_direction = j - previous_coords[1]
							if self.board[i+i_direction][j+j_direction]:
								return True
			except IndexError:
				pass
		return False		

	# Find a list of all squares adjacent to a certain square
	def adjacent_coordinates(self,x,y):
		coords = []
		for i in range(x-1, x+2):
			if i in range(3):
				for j in range(y-1, y+2):
					if j in range(3):
						coords.append((i, j))
		try:
			coords.remove((x,y))
		except ValueError as e:
			print("<!> Error: invalid indices passed to function. <!>")
		return coords
	
	def board_full(self):
		for i in self.board:
			for j in i:
				if j == "-":
					return False
		return True




if __name__ == '__main__':
	game = TicTacToeGame()
	game.start_game()
	