# Functions for setup.py

import turtle, time

# Used to create simple points
def create_point(x, y):
	pylon = turtle.Turtle()
	pylon.penup()
	pylon.color("red")
	pylon.shape("circle")
	pylon.goto(x, y)

	return pylon

class Drone(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.speed(1)

	def move_to(self, x, y):
		self.goto(x, y)

	def go_forward(self, n):
		self.forward(n)

	def go_backward(self, n):
		self.backward(n)
