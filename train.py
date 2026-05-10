import numpy as np
from environment import TicTacToe
from agent import QLearningAgent

env= TicTacToe()

agent_x= QLearningAgent(alpha= 0.2, gamma=0.9, epsilon=0.2)
agent_o= QLearningAgent(alpha= 0.2, gamma=0.9, epsilon=0.2)

EPISODES =50000

def train():
    print(f"Training starts now. There will be {EPISODES} tournaments.")

    wins_x = 0
    wins_o = 0
    draws = 0
    total_illegal_moves = 0

    for episode in range(1, EPISODES+1):
        state= env.reset()
        done= False

        current_player=1

        while not done:
            if current_player==1:
                current_agent= agent_x
            else:
                current_agent=agent_o

            action= current_agent.choose_action(state)
            next_state, reward, done = env.step(action,current_player)

            if reward ==-10 and not done:
                total_illegal_moves +=1

            current_agent.learn(state, action, reward, next_state, done)
            state= next_state

            if reward != -10:
                current_player *= -1       

        winner= env.checkWinner()
        if winner== 1:
            wins_x +=1
        elif winner == -1:
            wins_o +=1
        else:
            draws +=1   

        if agent_x.epsilon > 0.01: 
            agent_x.epsilon *= 0.9999
            agent_o.epsilon *= 0.9999

        if episode %500==0:
            print(f"episode:{episode}")
            print(f"Win X:{wins_x} | Win O:{wins_o} | Draws:{draws}")
            print(f"Illegal move count in the last 500: {total_illegal_moves}")

            wins_x, wins_o, draws, total_illegal_moves=0,0,0,0  

    print("Training completed.")

    
    
if __name__== "__main__":
    train()