"""
LESSON: 3.1 - Lines
TECHNIQUE 2: Declaring Points
PRACTICE 1
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

# Declare points
top_left = (0, 200)
top_right = (400, 200)
bottom_left = (200, 0)
bottom_right = (200, 400)

# Draw line
pygame.draw.line(window, (173, 216, 35), top_left, bottom_right, 2)
pygame.draw.line(window, (173, 216, 35), bottom_left, top_right, 2)
pygame.draw.line(window, (173, 216, 35), top_right, bottom_right, 2)
pygame.draw.line(window, (173, 216, 35), top_left, bottom_left, 2)


pygame.display.flip()
pygame.time.wait(5000)


# Turn in your Coding Exercise.

