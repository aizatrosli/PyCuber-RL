import pycuber as pc

colourArr = {"red": "[r]",
            "yellow": "[y]",
            "green": "[g]",
            "white": "[w]",
            "orange": "[o]",
            "blue": "[b]",
            "unknown": "[u]"}

def face_converter(face):
    #Convert pycuber colour array to normal colour array
    newface = []
    for srow in face:
        newrow = []
        for scubie in srow:
            newrow.append(str(scubie))
        newface.append(newrow)

    return newface, face

def face_centre(face):
    #Return colour of centre face
    face = face_converter(face)
    ccface = face[2][2]
    if ccface in colourArr:
        return ccface
    else:
        ccface = "[u]"
        return ccface