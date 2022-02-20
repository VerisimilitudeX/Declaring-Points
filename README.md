# Declaring Points
The pygame library gives us the tools to draw shapes. First the library must be imported and initialized, then a window opened, then you can draw lines inside the window at specific coordinate points.
# Drawing lines in Python using PyGame
* import pygame
* pygame.init()
* left = (100, 0)
* right = (200, 0)
* window = pygame.display.set_mode([400, 300])
* window.fill(255, 255, 255)
* pygame.draw.line(window, (255, 255, 255), left, right, 2)
* pygame.display.flip() 
