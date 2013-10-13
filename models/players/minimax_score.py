class MinimaxScorePlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.minimax(board)

  def minimax(self, board):
    return self.max_value(board, 10, -float('inf'), float('inf'))[1]

  def max_value(self, board, depth, alpha, beta):
    moves = board.valid_moves(self.color)
    if depth == 0:
      return self.get_score_weight(board), None
    if moves.__len__() == 0:
      if board.valid_moves(board._opponent(self.color)).__len__() == 0:
        return self.get_score_weight(board), None
      return self.min_value(board, depth-1, alpha, beta)
    ret_move = moves[0]
    for move in moves:
      if alpha >= beta:
        break
      test_board = board
      test_board.play(move, self.color)
      v = self.min_value(test_board, depth-1, alpha, beta)[0]
      if v > alpha:
        alpha = v
        ret_move = move
    return alpha, ret_move

  def min_value(self, board, depth, alpha, beta):
    moves = board.valid_moves(board._opponent(self.color))
    if depth == 0:
      return self.get_score_weight(board), None
    if moves.__len__() == 0:
      if board.valid_moves(self.color).__len__() == 0:
        return self.get_score_weight(board), None
      return self.max_value(board, depth-1, alpha, beta)
    ret_move = moves[0]
    for move in moves:
      if alpha >= beta:
        break
      test_board = board
      test_board.play(move, board._opponent(self.color))
      v = self.max_value(test_board, depth-1, alpha, beta)[0]
      if v < beta:
        beta = v
        ret_move = move
    return beta, ret_move



  def get_score_weight(self, board):
    total = 0
    for sq in board._squares():
        if board.get_square_color(sq/10, sq%10) == self.color:
          total += 1
        elif board.get_square_color(sq/10, sq%10) == board._opponent(self.color):
          total -= 1
    return total

  def print_moves(self, board, color):
    for move in board.valid_moves(color):
      print str(move.x) + " " + str(move.y)