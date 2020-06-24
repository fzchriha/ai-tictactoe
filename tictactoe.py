import random
class TicTacToe(object):
    def __init__(self):
      self.board = [
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"]
                ]

    def print_board(self, board):
      print("---------")
      for line in board:
        new_line = []
        for elem in line:
          if elem == '_':
            new_line.append(" ")
          else:
            new_line.append(elem)
        print("| "+ " ".join(new_line)+" |")
      print("---------")
    
    def board_not_filled(self):
      for line in self.board:
        if '_' in line:
          return True
      return False

    def not_empty(self, i, j):
      return self.board[i][j] != "_"

    def validate_move(self, player):
      if self.board_not_filled():
      # Make sure that there is still empty boards
        # Initial input
        #Coordinates follow cartesian graph
        move = raw_input("Enter the coordinates: ").split()
        x = move[0]
        y = move[-1]
        valid_move = [1, 2, 3]
        # Check if user input is a number
        if not x.isdigit() or not y.isdigit():
          print("You should enter numbers!")
          # Recursion
          self.validate_move(player)
        else:
          x = int(x)
          y = int(y)
          i = 3 - y
          j = x - 1
          # Check if the move chosen is valid
          # coordinates should be between 1 and 3
          # board should be empty
          if x not in valid_move or  y not in valid_move:
            print("Coordinates should be from 1 to 3!\n")
            self.validate_move(player)
          elif self.not_empty(i, j):
            print("This cell is occupied! Choose another one!\n")
            self.validate_move(player)
          else:
            self.board[i][j] = player
            return self.print_board(self.board)

    def smart_move(self, potential_move, player):
      #Horizontal check
      for i in range(3):
        line = ''
        for j in range(3):
          line += self.board[i][j]
        if line in potential_move:
          k = line.index('_')
          self.board[i][k] = player
          return self.print_board(self.board)

      # Vertical check
      for i in range(3):
        line = ''
        for j in range(3):
          line += self.board[j][i]
        if line in potential_move:
          k = line.index('_')
          self.board[k][i] = player
          return self.print_board(self.board)
      
      # \ check
      diagonal1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
      if diagonal1 in potential_move:
        k = diagonal1.index('_')
        self.board[k][k] = player
        return self.print_board(self.board)
      
      
      # / check
      diagonal2 = self.board[0][2] + self.board[1][1] + self.board[2][0]
      if diagonal2 in potential_move:
        k = diagonal2.index('_')
        self.board[k][2-k] = player
        return self.print_board(self.board)

      return 0

    def machine_move(self, player):
      if self.board_not_filled():
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        potential_wins = ["OO_", "O_O", "_OO"]
        potential_loss = ["XX_", "X_X", "_XX"]

        # Check for potential wins
        # Else check for potential losses
        # Else do a random move
        if self.smart_move(potential_wins, player) != 0:
          return self.smart_move(potential_wins, player)
        elif self.smart_move(potential_loss, player) != 0:
          return self.smart_move(potential_loss, player)
        elif self.not_empty(i,j):
          self.machine_move(player)
        else:
          self.board[i][j] = player
          return self.print_board(self.board)            
    
    def who_won(self):
        # Horizontal win
        for i in range(3):
          line = ""
          for j in range(3):
            line += self.board[i][j]
          if line == "XXX":
            return "X wins"
          elif line == "OOO":
            return "O wins"

        # Vertical win
        for i in range(3):
          line = ""
          for j in range(3):
            line += self.board[j][i]
          if line == "XXX":
            return "X wins"
          elif line == "OOO":
            return "O wins"
        
        # \ win
        diagonal1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diagonal1 == "XXX":
          return "X wins"
        elif diagonal1 == "OOO":
          return "O wins"
        
        # / win
        diagonal1 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diagonal1 == "XXX":
          return "X wins"
        elif diagonal1 == "OOO":
          return "O wins"


class TwoHumanPlayers(TicTacToe):
  def main(self):
      #Initial board
      self.print_board(self.board)
      while self.board_not_filled():
        print("Player 1, it's your turn!\n")
        self.validate_move("X")
        if self.who_won() == "X wins":
          return self.who_won()

        print("Player 2, show us what you got!!\n")
        self.validate_move("O")
        if self.who_won() == "O wins":
          return self.who_won()

      return "Draw"
    

class AIPlayer(TicTacToe):
  def main(self):
    #Initial board
    self.print_board(self.board)
    while self.board_not_filled():
      print("Human, it's your turn!\n")
      self.validate_move("X")
      if self.who_won() == "X wins":
        return self.who_won()

      self.machine_move("O")
      if self.who_won() == "O wins":
        return self.who_won()
    return "Draw"

 
  
  
  
def menu():
  choice = int(input("\tChoose 1 to play against a MACHINE: \n\tChoose 2 to play against a HUMAN: "))
  if choice == 1:
    tictactoe_version2 = AIPlayer()
    print(tictactoe_version2.main())
  elif choice == 2:
    tictactoe_version1 = TwoHumanPlayers()
    print(tictactoe_version1.main())
  else:
    print("Print a valid choice!")
    menu()    

menu()








