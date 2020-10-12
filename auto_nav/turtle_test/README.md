# Creating and running your algorithm

1. Copy template.py with `cp template.py filename.py` replacing "filename" with a name of your choice
2. Write your code in the auto_nav function
3. Run setup.py and then you will be prompted with the file name of your choice.
4. You're now good to go.

Note: If you get a display variable error, enter in the command `export DISPLAY=:0` and launch Xming.

# Function Specs For auto_nav()

### Parameters

* drone - the drone object that you'll be moving around
* pylon1 - coordinates of the first pylon of the form [x, y]
* pylon2 - coordinates of the second pylon of the form [x, y]

### Methods for the drone

* You may use whatever function is given by the turtle.Turtle() class unless told not to. Here's the documentation: https://docs.python.org/3/library/turtle.html
* The turtle.Turtle() class has the method setpos(), but try to use move_to() instead
