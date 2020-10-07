# Functions for setup.py

import turtle

# Used to create simple points
def create_point(x, y):
	pylon = turtle.Turtle()
	pylon.penup()
	pylon.color("red")
	pylon.shape("circle")
	pylon.goto(x, y)

	return pylon
