#### ---- SETUP ---- ####

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to size [400, 480], and assign result to a
# variable called window
window = pygame.display.set_mode([400,480])

# FILL the window with (255, 255, 255)
window.fill((255, 255, 255))

# Create a TUPLE with three values, (0, 0, 0) and
# assign to the variable black
# ---> TEST AFTER THIS LINE <--- #
black = (0, 0, 0)


#### ---- DRAW OUTLINE ---- ####

# DRAW LINES to make a face. For arguments, use window,
# black, and the two points provided in each comment.

# -- Profile (7 lines) --

# (160, 120), (120, 160)
pygame.draw.line(window, black, (160, 120), (120, 160), 2)

# (120, 160), (120, 240)
pygame.draw.line(window, black, (120, 160), (120, 240), 2)

# (120, 240), (80, 320)
pygame.draw.line(window, black, (120, 240), (80, 320), 2)

# (80, 320), (120, 320)
pygame.draw.line(window, black, (80, 320), (120, 320), 2)

# (120, 320), (120, 380)
pygame.draw.line(window, black, (120, 320), (120, 380), 2)

# (120, 380), (160, 400)
pygame.draw.line(window, black, (120, 380), (160, 400), 2)

# (160, 400), (200, 400)
pygame.draw.line(window, black, (160, 400), (200, 400), 2)


# -- Hair (5 Lines) --

# (160, 120), (160, 100)
pygame.draw.line(window, black, (160, 120), (160, 100), 2)

# (160, 100), (320, 100)
pygame.draw.line(window, black, (160, 100), (320, 100), 2)

# (320, 100), (320, 280)
pygame.draw.line(window, black, (320, 100), (320, 280), 2)

# (320, 280), (280, 280)
pygame.draw.line(window, black, (320, 280), (280, 280), 2)

# (280, 280), (160, 120)
pygame.draw.line(window, black, (280, 280), (160, 120), 2)


# -- Neck (1 Line) --

# (290, 280), (290, 400)
pygame.draw.line(window, black, (290, 280), (290, 400), 2)


#### ---- DRAW FACIAL FEATURES ---- ####

# -- Eye (4 Lines) --

# (170, 220), (140, 240)
pygame.draw.line(window, black, (170, 220), (140, 240), 2)

# (170, 220), (200, 240)
pygame.draw.line(window, black, (170, 220), (200, 240), 2)

# (170, 255), (140, 240)
pygame.draw.line(window, black, (170, 255), (140, 240), 2)

# (170, 255), (200, 240)
pygame.draw.line(window, black, (170, 255), (200, 240), 2)


# -- Pupil (3 Lines) --

# (170, 220), (170, 240)
pygame.draw.line(window, black, (170, 220), (170, 240), 2)

# (170, 240), (155, 240)
pygame.draw.line(window, black, (170, 240), (155, 240), 2)

# (155, 240), (155, 230)
pygame.draw.line(window, black, (155, 240), (155, 230), 2)


# -- Mouth (2 Lines) --

# (120, 340), (170, 340)
pygame.draw.line(window, black, (120, 340), (170, 340), 2)

# (170, 340), (190, 330)
pygame.draw.line(window, black, (170, 340), (190, 330), 2)


#### ---- FINISH ---- ####

# FLIP the display
pygame.display.flip()

# Get input to pause the program
input("Please press the Enter key to proceed")
