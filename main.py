import random
from ast import literal_eval
from os import path
import sys,pygame

import gym
import gym_game
import numpy as np


def usage():
    print('Correct usage for the program is python [program_name] [image_location] [sensor_range] [sigma_nose_values] [lane_Prescision]')
    exit(-1)
def listedFileNotFoundError():
    print('Listed file not found...')
    exit(-1)

def unknownError():
    print('Unknown error detected')
    exit(-1)
try:
    userInput = sys.argv
    if len(userInput)!=4:
        raise IndexError
    if type(literal_eval(userInput[2]))!=int or type(literal_eval(userInput[3]))!=int or type(userInput[1])!=str:
        raise ValueError
    if not path.isfile(userInput[1]):
        raise FileNotFoundError
except (IndexError,SyntaxError,ValueError):
    usage()
except FileNotFoundError:
    listedFileNotFoundError()
except:
    unknownError()



def simulate():
    global epsilon, epsilon_decay
    for episode in range(MAX_EPISODES):

        # Init environment
        state = env.reset()
        total_reward = 0

        # AI tries up to MAX_TRY times
        for t in range(MAX_TRY):

            # In the beginning, do random action to learn
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state])

            # Do action and get result
            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            # Get correspond q value from state, action pair
            q_value = q_table[state][action]
            best_q = np.max(q_table[next_state])

            # Q(state, action) <- (1 - a)Q(state, action) + a(reward + rmaxQ(next state, all actions))
            q_table[state][action] = (1 - learning_rate) * q_value + learning_rate * (reward + gamma * best_q)
            # Set up for the next iteration
            state = next_state

            # Draw games
            env.render()

            # When episode is done, print reward
            if done or t >= MAX_TRY - 1:
                print("Episode %d finished after %i time steps with total reward = %f." % (episode, t, total_reward))
                break

        # exploring rate decay
        if epsilon >= 0.005:
            epsilon *= epsilon_decay


if __name__ == "__main__":
    env = gym.make("Pygame-v0")
    MAX_EPISODES = 9999
    MAX_TRY = 1000
    epsilon = 1
    epsilon_decay = 0.999
    learning_rate = 0.1
    gamma = 0.6
    num_box = tuple([1201,601])
    q_table = np.zeros(num_box + (env.action_space.n,))
    simulate()