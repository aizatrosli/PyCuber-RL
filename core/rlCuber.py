import random
from .utils import cubeparser

movementDict = {1:["U","R","F","D","L","B"],
                2:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'"],
                3:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'", "M", "M'", "E", "E'", "S", "S'"],
                4:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'","M", "M'", "E", "E'", "S", "S'","U2","R2","F2","D2","L2","B2"],
                5:["U", "R", "F", "D", "L", "B", "U'", "R'", "F'", "D'", "L'", "B'","M", "M'", "E", "E'", "S", "S'", "U2", "R2", "F2", "D2", "L2",
                    "B2", "u", "r", "f", "d", "l", "b", "u'", "r'", "f'", "d'", "l'", "b'"]}
facesArrOld = ["B","D","L","F","R","U"]
facesArr = ["F","B","U","B","L","R"]

class rlcuber(object):
    def __init__(self,difficulty=1,scramble=True):
        self.diff = difficulty
        self.action_space = Space(int(len(movementDict.get(self.diff))))
        self.observation_space = Space(int(3*3*len(facesArr))-6)
        if scramble:
            self.reset()
        else:
            self.cuber = cubeparser()


    def step(self,movement,cube=False):
        move = movementDict.get(self.diff)[movement-1]
        if self.scramble_done:
            self.movementArr.append(move)
        movement = self.cuber.cube_move(move)
        observation = self.cuber.cube_states() if cube else self.cuber.faces_states()
        reward = 1 if self.cuber.cube_solved() else 0
        done = True if reward > 0 else False
        return observation, reward, done

    def render(self):
        print(self.cuber.render_colour())

    def reset(self, scramble=True, cube=True):
        self.cuber = cubeparser()
        self.movementArr = []
        if scramble:
            self.scramble_done = False
            self.scramble_state, self.scramble_arr = self.scramble()
            self.scramble_done = True
        if cube:
            return self.cuber.cube_states()
        else:
            return self.cuber.faces_states()

    def reset_same(self, cube=True):
        if len(self.scramble_arr) > 0:
            self.cuber = cubeparser()
            self.movementArr = []
            self.scramble_done = False
            for move in self.scramble_arr:
                _o, _r, _d = self.step(move)
            self.scramble_done = False
        else:
            self.reset()
        if cube:
            return self.cuber.cube_states()
        else:
            return self.cuber.faces_states()


    def scramble(self,moveval=None):
        observation = self.observation_space.n
        scrambleArr = []
        if moveval == None:
            while (observation > 0):
                move = random.randint(0,self.action_space.n-1)
                scrambleArr.append(move)
                observation, _r, _d = self.step(move,cube=True)
        else:
            targetobservation=observation-moveval
            if targetobservation > 0:
                while (observation > 0):
                    move = random.randint(0, self.action_space.n - 1)
                    scrambleArr.append(move)
                    observation, _r, _d = self.step(move, cube=True)
            else:
                print("O")

        return observation, scrambleArr

    def scramble_move(self):
        return self.scramble_arr

    def convert_movement(self,arr=[0]):
        realmove = []
        if "list" in str(type(arr)):
            print("Converted")
            arr = self.scramble_arr
        else:
            arr = [arr]
        for move in arr:
            print(move)
            realmove.append(movementDict.get(self.diff)[move - 1])
        return realmove


    def compare(self):
        movementrefArr = self.cuber.normal_solver()
        print("RefMovement : " + str(movementrefArr))
        print("DOEMovement : " + str(self.movementArr))
        if len(self.movementArr) < len(movementrefArr):
            return True
        else:
            return False


class Space(object):
    def __init__(self, n):
        self.n = n
    def sample(self):
        return random.randint(0, self.n)
    def __repr__(self):
        return "Space(%d)" % self.n