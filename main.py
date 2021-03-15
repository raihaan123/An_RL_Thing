import numpy as np
from agent import Agent
from environment import Environment

environment = Environment()

environment.create_agent()


for i in range(10):
    environment.update()