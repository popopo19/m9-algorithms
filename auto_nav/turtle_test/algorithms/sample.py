# Sample Algorithm

# Some functions for drone movement
# move_to(x, y) - will move the drone to position (x, y)
# go_foward(n) - will move the drone forward n amount
# go_backward(n) - will move the drone backward n amount
# left(n) - will rotate drone left n degrees
# right(n) - will rotate drone right n degrees

import turtle

def auto_nav(drone, pylon1, pylon2):
	for i in range(8):
		drone.move_to(pylon1[0] + 30, pylon1[1] - 30)
		drone.move_to(pylon2[0] + 30, pylon2[1] + 30)
		drone.move_to(pylon2[0] - 30, pylon2[1] + 30)
		drone.move_to(pylon1[0] - 30, pylon1[1] - 30)

# GOOD LUCK
