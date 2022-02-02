"""
LESSON: 3.1 - Lines
TECHNIQUE 3: Line Thickness
PRACTICE 1
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

# Declare points
point_1 = (0, 200)
point_2 = (100, 200)
point_3 = (200, 200)
point_4 = (300, 200)
point_5 = (400, 200)

# Draw lines
pygame.draw.line(window, (212, 255, 255), point_1, point_2, 7)
pygame.draw.line(window, (214, 255, 255), point_2, point_3, 8)
pygame.draw.line(window, (193, 255, 255), point_3, point_4, 9)
pygame.draw.line(window, (169, 255, 255), point_4, point_5, 10)


pygame.display.flip()
pygame.time.wait(5000)


# Turn in your Coding Exercise.

