class WindowsMediaPlayer:
  def __init__(self, color):
    self.color = color
    self.weight = [ 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0,
                    0, 120, -20,  20,   5,   5,  20, -20, 120, 0,
                    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20, 0,
                    0, 20,  -5,  15,   3,   3,  15,  -5,  20, 0,
                    0, 5,  -5,   3,   3,   3,   3,  -5,   5, 0,
                    0, 5,  -5,   3,   3,   3,   3,  -5,   5, 0,
                    0, 20,  -5,  15,   3,   3,  15,  -5,  20, 0,
                    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20, 0,
                    0, 120, -20,  20,   5,   5,  20, -20, 120, 0,
                    0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0
                ]

  def play(self, board):
    return self.get_best_score(board)

  def get_best_score(self, board):
    best_score = -float('inf')
    ret_move = None
    for move in board.valid_moves(self.color):
      test_board = board
      test_board.play(move, self.color)
      score = self.get_score_weight(test_board)
      if score > best_score:
        best_score = score
        ret_move = move
    return ret_move

  def get_score_weight(self, board):
    total = 0
    for sq in board._squares():
        if board.get_square_color(sq/10, sq%10) == self.color:
          total += self.weight[sq]
        elif board.get_square_color(sq/10, sq%10) == board._opponent(self.color):
          total -= self.weight[sq]
    return total

  def print_moves(self, board):
    for move in board.valid_moves(self.color):
      print str(move.x) + " " + str(move.y)