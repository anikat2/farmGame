from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from vpython import vector
import numpy as np

app = Ursina()

class Boox(Button):
    def __init__(self, position=(5,0,5)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9,1.0)),
            highlight_color = color.lime
        )
class Fence(Button):
    def __init__(self, position=(5,0,5)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'fence1.obj',
            scale = 0.005,
            origin_y = 0,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9,1.0)),
            highlight_color = color.lime
        )
        self.rotation = vector(0, 90, 0)
for z in range(50):
    for x in range(50):
        boox = Boox(position = (x,0,z))

#House
for z in range (5, 16):
        for y in range (1, 10):
            boox = Boox(position = (16,y,z))
for x in range (5, 16):
    for y in range (1, 10):
        boox = Boox(position = (x,y,5))
for x in range (5, 10):
    for y in range (1, 3):
        boox = Boox(position = (x,y,16))
for x in range (12, 17):
    for y in range (1, 3):
        boox = Boox(position = (x,y,16))
for x in range (5, 17):
    for y in range (3, 10):
        boox = Boox(position = (x,y,16))
for z in range (5, 16):
    for y in range (1, 10):
        boox = Boox(position = (5,y,z))
    #Roof
for z in range(5,16):
    for x in range(5, 16):
        boox = Boox(position = (x,9,z))
#Farm lining
for z in range (16, 50):
        f = Fence(position = (50,0,z))
for x in range (0, 50):
        f = Fence(position = (x,0,50))
for x in range (0, 5):
        f = Fence(position = (x,0,16))
for x in range (17, 50):
        f = Fence(position = (x,0,16))
for z in range (16, 50):
        f = Fence(position = (0,0,z))

player = FirstPersonController()
app.run()
