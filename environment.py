import numpy as np

class TicTacToe:
    def __init__(self):
        self.board= np.zeros(9)
        self.current_player=1

    def reset(self):
        self.board= np.zeros(9)
        return self.board
    
    