import pygame

pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

top = (200, 0)
left = (0, 150)
right = (400, 150)
bottom_left = (50, 400)
bottom_right = (350, 400)

pygame.draw.line(window, (154, 214, 73), top, bottom_left, 2)
pygame.draw.line(window, (154, 214, 73), top, bottom_right, 2)
pygame.draw.line(window, (154, 214, 73), left, right, 2)
pygame.draw.line(window, (154, 214, 73), left, bottom_right, 2)
pygame.draw.line(window, (154, 214, 73), bottom_left, right, 2)

pygame.display.flip()
pygame.time.wait(5000)
