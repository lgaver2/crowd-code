#https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118
from p5 import setup, draw, size, background, run, Vector, stroke, circle
import numpy as np
class Boid():

    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)

        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = Vector(*vec) 

    def show(self):
        stroke(255)
        circle((self.position.x, self.position.y), radius=10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration