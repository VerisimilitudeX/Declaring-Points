"""
LESSON: 3.1 - Lines
TECHNIQUE 3: Line Thickness
PRACTICE 2
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

# Colors
red = (200, 0, 0)
yellow = (255, 255, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

# Declare points
left = (0, 200)
right = (400, 200)

# Draw lines
pygame.draw.line(window, red, left, right, 50)
pygame.draw.line(window, yellow, left, right, 45)
pygame.draw.line(window, green, left, right, 40)
pygame.draw.line(window, blue, left, right, 15)

pygame.display.flip()
pygame.time.wait(5000)


# Turn in your Coding Exercise.

