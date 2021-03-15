import numpy as np
from agent import Agent

class Environment:

    def __init__(self):

        self.state = np.zeros((5,5))


    def create_agent(self):

        init_state = np.random.choice(self.state.shape[0], 2, replace=False)
        self.agent = Agent(init_state)


    def Reward(self):

        if np.array_equal(self.agent.state, np.array([0, 1]) ):
            return(10)

        elif np.array_equal(self.agent.state, np.array([0, 3]) ):
            return(5)

        elif (self.agent.state > 4).any() or (self.agent.state < 0).any():
            return(-1)
        
        else:
            return(0)

    def update(self):

    
        print(f"Before update State: {self.agent.state}")

        self.agent.take_action()
        print(f"New action: {self.agent.action}")

        self.agent.state += self.agent.action
        self.agent.reward += self.Reward()
        
        self.agent.state[self.agent.state > 4] = 4
        self.agent.state[self.agent.state < 0] = 0

        print(f"Updated State: {self.agent.state}")
        print(f"Reward: {self.agent.reward}")
