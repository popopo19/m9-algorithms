# Sample Algorithm

# Some functions for turtle movement
# drone.left(n) - Turn left n degrees. There's also right.
# drone.go_foward(n) - Go forward n amount. There's also backwards.
# drone.move_to(x, y) - Got to position (x, y)

import turtle

def auto_nav(drone, pylon1, pylon2):
	for i in range(2):
		drone.move_to(pylon1[0] + 30, pylon1[1] - 30)
		drone.move_to(pylon2[0] + 30, pylon2[1] + 30)
		drone.move_to(pylon2[0] - 30, pylon2[1] + 30)
		drone.move_to(pylon1[0] - 30, pylon1[1] - 30)

# GOOD LUCK