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

# Sorting time algorithm via binary search
def sort_by_time(order, new_row):
	temp_order = []
	temp_order += order
	print("temp: " + str(temp_order))

	index = len(temp_order) // 2

	while len(temp_order) > 1:
		if temp_order[len(temp_order) // 2][1] < new_row[1]:
			temp_order = temp_order[len(temp_order) // 2:]
			index += len(temp_order) // 2
		elif temp_order[len(temp_order) // 2][1] > new_row[1]:
			temp_order = temp_order[:len(temp_order) // 2 + 1]
			index -= len(temp_order) // 2
		else:
			index = len(temp_order) // 2
			break
		print(temp_order)
		print(index)

	if temp_order[0][1] >= new_row[1]:
		index += 1
	else:
		index -= 1

	order.insert(index, new_row)
	return order

class Drone(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.speed(1)
		self.wait_time = 1

	def move_to(self, x, y):
		self.goto(x, y)
		time.sleep(self.wait_time)

	def go_forward(self, n):
		self.forward(n)
		time.sleep(self.wait_time)

	def go_backward(self, n):
		self.backward(n)
		time.sleep(self.wait_time)
