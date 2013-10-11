from models.board import Board
from math import sqrt

class ScorePlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.get_best_score(board)

  def get_best_score(self, board):
    best_score = 0
    ret_move = None
    for move in board.valid_moves(self.color):
      test_board = board
      test_board.play(move, self.color)
      if self.color == Board.WHITE:
        score = test_board.score()[0]
      else:
        score = test_board.score()[1]
      if score > best_score:
        best_score = score
        ret_move = move
      elif score == best_score:
        ret_move = self.getNearestCorner([move, ret_move])
    return ret_move

  def getNearestCorner(self, moves):
    corners = [[1,1],[1,8], [8,1], [8,8]]    
    minDist = 10
    retMove = None
    for move in moves:
      for corner in corners:
        distX = abs(corner[0] - move.x)
        distY = abs(corner[1] - move.y)
        dist  = sqrt(distX*distX + distY*distY)       
        if dist < minDist:
          minDist = dist
          retMove = move
          
          
    return retMove

  def print_moves(self, board):
    for move in board.valid_moves(self.color):
      print str(move.x) + " " + str(move.y)


