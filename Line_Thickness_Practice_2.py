import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

red = (200, 0, 0)
yellow = (255, 255, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

left = (0, 200)
right = (400, 200)

pygame.draw.line(window, red, left, right, 50)
pygame.draw.line(window, yellow, left, right, 45)
pygame.draw.line(window, green, left, right, 40)
pygame.draw.line(window, blue, left, right, 15)

pygame.display.flip()
pygame.time.wait(5000)
