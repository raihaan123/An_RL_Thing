import numpy as np

class Agent:

    def __init__(self, init_state):
        
        self.state = init_state
        self.action_space = np.array([ [1, 0],
                                  [-1, 0],
                                  [0, 1],
                                  [0, -1]  ])
        self.reward = 0

    def take_action(self):
        self.action = self.action_space[np.random.randint(self.action_space.shape[0] - 1), :]