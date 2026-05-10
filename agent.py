import numpy as np

class QLearningAgent:
    def __init__(self, alpha= 0.2, gamma=0.95, epsilon=0.2):
        self.alpha= alpha #learning rate(how fast does the agent learn)
        self.gamma= gamma #vision (should i get the small reward now or wait and get the bigger reward)
        self.epsilon= epsilon #how much does the agent explore

        self.q_table={} #empty q-table


    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state]= np.zeros(9)

        return self.q_table[state]
    #if the state wasn't used before, it gets a zero value.
    #if the state was already there, it returns the q-value
    
    def choose_action(self,state):
        if np.random.uniform(0,1)< self.epsilon:
            action= np.random.randint(0,9)
            #exploration
        else:
            q_values= self.get_q_values(state)
            action=np.argmax(q_values)

        return action
    
    def learn(self, state, action, reward, next_state, done):
        currentQValue = self.get_q_values(state)#get the q-table for that state
        oldValue= currentQValue[action] # gets the q-value of that action
                                                
        if done:
            next_max=0
        else:
            next_q_value=self.get_q_values(next_state)
            next_max= np.max(next_q_value)

        new_value= oldValue+ self.alpha * (reward+self.gamma *next_max-oldValue)
        self.q_table[state][action]= new_value