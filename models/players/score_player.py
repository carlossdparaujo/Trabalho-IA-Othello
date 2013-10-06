from models.board import Board

class ScorePlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.get_best_score(board)

  def get_best_score(self, board):
    best_score = 0
    ret_move = None
    self.print_moves(board)
    for move in board.valid_moves(self.color):
      test_board = board
      test_board.play(move, self.color)
      if self.color == Board.WHITE:
        score = test_board.score()[0]
      else:
        score = test_Board.score()[1]
      if score > best_score:
        ret_move = move
    return ret_move


  def print_moves(self, board):
    for move in board.valid_moves(self.color):
      print str(move.x) + " " + str(move.y)


