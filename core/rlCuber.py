import random
from .utils import cubeparser

movementDict = {1:["U","R","F","D","L","B"],
                2:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'"],
                3:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'", "M", "M'", "E", "E'", "S", "S'"],
                4:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'","M", "M'", "E", "E'", "S", "S'","U2","R2","F2","D2","L2","B2"],
                5:["U", "R", "F", "D", "L", "B", "U'", "R'", "F'", "D'", "L'", "B'","M", "M'", "E", "E'", "S", "S'", "U2", "R2", "F2", "D2", "L2",
                    "B2", "u", "r", "f", "d", "l", "b", "u'", "r'", "f'", "d'", "l'", "b'"]}
facesArr = {"B","D","L","F","R","U"}

class rlcuber(object):
    def __init__(self,difficulty=1):
        self.diff = difficulty
        self.reset()

    def step(self,movement):
        move = movementDict.get(self.diff)[movement-1]
        if self.scramble_done:
            self.movementArr.append(move)
        cube = self.cuber.cube_move(move)
        observation = self.cuber.cube_states()
        reward = 1 if self.cuber.cube_solved() else 0
        done = True if reward > 0 else False

        return observation, reward, done

    def render(self):
        print(self.cuber.render_colour())

    def reset(self, scramble=True):
        self.cuber = cubeparser()
        self.movementArr = []
        if scramble:
            self.scramble_done = False
            self.scramble_state, self.scramble_arr = self.scramble()
            self.scramble_done = True
        return self.cuber.cube_states()

    def reset_same(self):
        if self.scramble_arr > 0:
            self.cuber = cubeparser()
            self.movementArr = []
            self.scramble_done = False
            for move in self.scramble_arr:
                _o, _r, _d = self.step(move)
            self.scramble_done = False
        else:
            self.reset()
        return self.cuber.cube_states()



    def observation_spacen(self):
        return int(3*3*len(facesArr))

    def action_spacen(self):
        return int(len(movementDict.get(self.diff)))

    def scramble(self):
        observation = self.observation_spacen()
        scrambleArr = []
        while (observation > 0):
            move = random.randint(0,self.action_spacen()-1)
            scrambleArr.append(move)
            observation, _r, _d = self.step(move)
        return observation, scrambleArr

    def scramble_move(self):
        return self.scramble_arr

    def compare(self):
        movementrefArr = self.cuber.normal_solver()
        print("RefMovement : " + str(movementrefArr))
        print("DOEMovement : " + str(self.movementArr))
        if len(self.movementArr) < len(movementrefArr):
            return True
        else:
            return False


