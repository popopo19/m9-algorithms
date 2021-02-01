# This is the test file to run when testing out your python file
# We will test algorithms using the turtle library
# Turtle documentation: https://docs.python.org/3/library/turtle.html

# IMPORTANT: The distance between the two pylons are not to-scale.
# Only the distance between the drone, destination, and pylon1 are to-scale.

import random, math, sys, threading, turtle
from functions import *

# Allows modules from the algorithms folder
sys.path.append("./algorithms")

# For lowering all turtles so points don't go offscreen
y_offset = -100

# Given pylon points
pylon1_coord = [0, y_offset + math.sqrt(30000)] * [2, 3]
pylon2_coord = [0, y_offset + math.sqrt(30000) + 200]

# Variable for when testing has stopped
done_testing = False

# Stopwatch for testing
stopwatch = 0


# Function for the threading
def start_stopwatch():
    global stopwatch

    while not done_testing:
        time.sleep(0.1)
        stopwatch += 0.1
    # print("Time: " + str(stopwatch))


def main():
    # Creates the screen
    win = turtle.Screen()

    # Creation of the drone
    drone = turtle.Turtle()
    drone.speed(1)
    drone.penup()
    drone.goto(-100, y_offset)
    drone.shape("turtle")
    drone.left(random.randrange(0, 361))
    drone.pendown()

    # Creation of pylons
    pylon1 = create_point(pylon1_coord[0], pylon1_coord[1])
    pylon2 = create_point(pylon2_coord[0], pylon2_coord[1])

    # Creation of destination point
    dest = create_point(100, y_offset)
    dest.color("blue")

    # Choose which algorithm to test
    test_file = input("Enter the file you want to test: ")
    algo = __import__(test_file)

    t = threading.Thread(target=start_stopwatch)
    t.start()
    algo.auto_nav(drone, pylon1.pos(), pylon2.pos())
    done_testing = True

    print("Time Taken: " + str(stopwatch))

    print("Execution Done. Click on turtle screen to exit program.")
    turtle.exitonclick()  # Ensures that screen will close on any key pressed


if __name__ == "__main__":
    main()
