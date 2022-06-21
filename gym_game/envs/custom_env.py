import gym
from gym import spaces
import numpy as np
from gym_game.envs.sampleSpace import startSampleSpaceEnv

class CustomEnv(gym.Env):
    def __init__(self):
        self.pygame = startSampleSpaceEnv()