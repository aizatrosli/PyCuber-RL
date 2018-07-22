import pycuber as pc
from pycuber.solver import CFOPSolver

colourArr = {"[r]","[y]","[g]","[w]","[o]","[b]","[u]"}
facesArr = {"B","D","L","F","R","U"}
scramble_ref = ""

class cubeparser(object):
    def __init__(self):
        self.cube = pc.Cube()
        self.cube_ref = pc.Cube()


    def face_converter(self, face):
        #Convert pycuber colour array to normal colour array
        face = self.cube.get_face(face)
        newface = []
        for srow in face:
            newrow = []
            for scubie in srow:
                newrow.append(str(scubie))
            newface.append(newrow)

        return newface, face

    def face_centre(self, face):
        #Return colour of centre face
        face, _ = self.face_converter(face)
        ccface = face[1][1]
        if ccface in colourArr:
            return ccface
        else:
            ccface = "[u]"
            return ccface

    def face_solved(self, face):
        #Return boolean if face is solved
        centre = self.face_centre(face)
        face, _ = self.face_converter(face)
        for srow in face:
            for scubie in srow:
                if not scubie in centre:
                    return False
        return True

    def cube_solved(self):
        #Return boolean if cube is solved
        for face in facesArr:
            if not self.face_solved(face):
                return False
        return True
    def face_states(self, face):
        #Return value total colour correct on face
        centre = self.face_centre(face)
        face, _ = self.face_converter(face)
        state = -1
        for srow in face:
            for scubie in srow:
                if  scubie in centre:
                    state += 1
        return state

    def cube_states(self):
        #Return value total colour correct on each faces
        state = 0
        for face in facesArr:
            state += self.face_states(face)
        return state

    def render_colour(self):
        return self.cube

    def cube_move(self,movement):
        self.scramble_ref = self.cube_ref(movement)
        return self.cube(movement)

    def normal_solver(self):
        solution = CFOPSolver(self.scramble_ref).solve(suppress_progress_messages=True)
        return solution