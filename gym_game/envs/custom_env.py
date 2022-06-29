import gym
from gym import spaces
import numpy as np
from gym_game.envs.sampleSpace import startSampleSpaceEnv

class CustomEnv(gym.Env):

    def __init__(self):
        self.pygame = startSampleSpaceEnv((1200, 600))
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=np.array([0,0]),high=np.array([1200,600]),dtype=np.int)
    def reset(self):
        del self.pygame
        self.pygame = startSampleSpaceEnv((1200, 600))
        obs = self.pygame.observe()
        return obs

    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate(obs)
        done = self.pygame.is_done()
        return obs,reward,done,{}

    def render(self,mode="human",close=False):
        return self.pygame.view()

