import pycuber as pc
import logging
from utils import cubeparser

movementDict = {1:["U","R","F","D","L","B"],
                2:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'"],
                3:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'", "M", "M'", "E", "E'", "S", "S'"],
                4:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'","M", "M'", "E", "E'", "S", "S'","U2","R2","F2","D2","L2","B2"],
                5:["U", "R", "F", "D", "L", "B", "U'", "R'", "F'", "D'", "L'", "B'","M", "M'", "E", "E'", "S", "S'", "U2", "R2", "F2", "D2", "L2",
                    "B2", "u", "r", "f", "d", "l", "b", "u'", "r'", "f'", "d'", "l'", "b'"]}


class rlcuber(object):
    def __init__(self,difficulty = 1):
        self.diff = difficulty
        self.reset()

    def step(self,movement):
        cube = self.cuber.cube_move(movement)
        observation = self.cuber.cube_states()
        reward = 1 if self.cuber.cube_solved() else reward = 0
        done = True if reward > 0 else done = False

        return observation, reward, done

    def render(self):
        print(self.cuber.render_colour())

    def reset(self):
        self.cuber = cubeparser()