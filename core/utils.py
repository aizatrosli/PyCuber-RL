import pycuber as pc

colourDict = {"red": "[r]",
            "yellow": "[y]",
            "green": "[g]",
            "white": "[w]",
            "orange": "[o]",
            "blue": "[b]",
            "unknown": "[u]"}

facesArr = {"B","D","L","F","R","U"}

class cubeparser(object):
    def __init__(self):
        self.cube = pc.Cube()


    def face_converter(self, face, cube=self.cube):
        #Convert pycuber colour array to normal colour array
        face = cube.get_face(face)
        newface = []
        for srow in face:
            newrow = []
            for scubie in srow:
                newrow.append(str(scubie))
            newface.append(newrow)

        return newface, face

    def face_centre(self, face):
        #Return colour of centre face
        face, _ = face_converter(face)
        ccface = face[2][2]
        if ccface in colourArr:
            return ccface
        else:
            ccface = "[u]"
            return ccface

    def face_solved(self, face):
        #Return boolean if face is solved
        centre = face_centre(face)
        face, _ = face_converter(face)
        for srow in face:
            for scubie in srow:
                if not scubie in centre:
                    return False
        return True

    def cube_solved(self):
        #Return boolean if cube is solved
        for face in facesArr:
            if not face_solved(face):
                return False
        return True
    def face_states(self, face):
        #Return value total colour correct on face
        centre = face_centre(face)
        face, _ = face_converter(face)
        state = 0
        for srow in face:
            for scubie in srow:
                if  scubie in centre:
                    state += 1
        return state

    def cube_states(self):
        #Return value total colour correct on each faces
        state = 0
        for face in facesArr:
            state += face_states(face)
        return state

    def render_colour(self):
        return self.cube

    def cube_move(self,movement):
        return self.cube(movement)