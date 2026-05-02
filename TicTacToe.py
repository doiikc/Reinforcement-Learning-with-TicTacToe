import numpy as np

class TicTacToe:
    def __init__(self):
        self.board= np.zeros((3,3),dtype=int)

    def reset(self):
        self.board= np.zeros((3,3), dtype=int)
        return self.board
    
    def render(self):
        print(self.board)

    def checkWinner(self):

        for i in [0,1]:

            sums= np.sum(self.board, axis=i)
            if 3 in sums:
                return 1
            if -3 in sums:
                return -1
            
            diagonal1= np.trace(self.board)
            diagonal2=np.trace(np.fliplr(self.board))

            if diagonal1==3 or diagonal2==3:
                return 1
            if diagonal1==-3 or diagonal2==-3:
                return -1
            
            if not 0 in self.board:
                return 0
            
        return None
    
    def step(self, action, player):
        row, col= divmod(action, 3)
        reward=0
        done=False

        if self.board[row,col] != 0:
            reward = -10
            done= True
            return tuple(self.board.reshape(9))
        
        self.board[row,col]=player

        winner= self.checkWinner()

        if winner == player:
            reward=10
            done=True
        elif winner == -player:
            reward= -10
            done=True
        elif winner==0:
            reward=2
            done=True
        else:
            reward=0
            done=False

        return tuple(self.board.reshape(9)), reward, done