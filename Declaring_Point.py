import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

top_left = (100, 100)
top_right = (300, 100)
bottom_left = (100, 300)
bottom_right = (300, 300)

pygame.draw.line(window, (0, 0, 0), top_left, top_right)
pygame.draw.line(window, (0, 0, 0), top_left, bottom_left)
pygame.draw.line(window, (0, 0, 0), top_right, bottom_right)
pygame.draw.line(window, (0, 0, 0), bottom_left, bottom_right)
pygame.draw.line(window, (0, 0, 0), top_left, bottom_right)
pygame.draw.line(window, (0, 0, 0), bottom_left, top_right)



pygame.display.flip()
pygame.time.wait(5000)
