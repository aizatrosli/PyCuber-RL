import pycuber as pc
import logging

movementDict = {1:["U","R","F","D","L","B"],
                2:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'"],
                3:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'", "M", "M'", "E", "E'", "S", "S'"],
                4:["U","R","F","D","L","B","U'","R'","F'","D'","L'","B'","M", "M'", "E", "E'", "S", "S'","U2","R2","F2","D2","L2","B2"],
                5:["U", "R", "F", "D", "L", "B", "U'", "R'", "F'", "D'", "L'", "B'","M", "M'", "E", "E'", "S", "S'", "U2", "R2", "F2", "D2", "L2",
                    "B2", "u", "r", "f", "d", "l", "b", "u'", "r'", "f'", "d'", "l'", "b'"]}

