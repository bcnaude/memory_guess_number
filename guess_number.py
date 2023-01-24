# implementation of card game - Memory
# Copy and paste this code into the CodeSkulptor editor at https://py2.codeskulptor.org/ to run.

import simplegui
import random

WIDTH = 50
HEIGHT = 100

numlist = []
exposed = []
moves = 0
state = 0
choices = [-1, -1]

# helper function to initialize globals
def init():
    """Starts new game, sets up shuffled card numbers"""
    global numlist, exposed, moves, state, choices
    numlist = range(0, 8)
    numlist.extend(range(0, 8))
    random.shuffle(numlist)
    random.shuffle(numlist)
    exposed = [0] * 16
    moves = 0
    state = 0
    choices = [-1, -1]
    l.set_text("Moves = " + str(moves))


# define event handlers
def mouseclick(pos):
    """Defines choices and whether clicked cards match, counts number of moves"""
    global choices, state, moves
    index = int(pos[0] / WIDTH)
    if state == 0:
        if exposed[index] == 0:
            if numlist[choices[0]] != numlist[choices[1]]:
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[index] = 1
            state = 1
            choices[0] = index
    elif state == 1:
        if exposed[index] == 0:
            state = 0
            exposed[index] = 1
            choices[1] = index
            moves = moves + 1
            l.set_text("Moves = " + str(moves))


# cards are logically 50x100 pixels in size
def draw(canvas):
    for index in range(0, len(numlist)):
        if exposed[index] == 0:
            canvas.draw_polygon(
                [
                    (WIDTH * index, 0),
                    (WIDTH * (index + 1), 0),
                    (WIDTH * (index + 1), 100),
                    (WIDTH * index, 100),
                ],
                3,
                "purple",
                "white",
            )
        else:
            canvas.draw_text(
                str(numlist[index]), [WIDTH * index + 5, HEIGHT - 25], 60, "blue"
            )


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
